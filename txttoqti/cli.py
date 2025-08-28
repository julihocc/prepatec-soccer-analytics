"""
Command-line interface for txt-to-qti library

Provides a unified CLI for all conversion functionality.
"""

import sys
import argparse
from pathlib import Path
from typing import List, Optional

from . import __version__
from .converter import TxtToQtiConverter
from .smart_converter import SmartConverter
from .exceptions import TxtToQtiError


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog='txt-to-qti',
        description='Convert plain text question banks to Canvas LMS QTI packages',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  txt-to-qti questions.txt                    # Basic conversion
  txt-to-qti questions.txt -o exam.zip        # Custom output name
  txt-to-qti questions.txt --smart            # Smart conversion (default)
  txt-to-qti questions.txt --force            # Force regeneration
  txt-to-qti --status questions.txt           # Show file status
  txt-to-qti --preview questions.txt          # Preview conversion
  txt-to-qti --batch *.txt                    # Convert multiple files
  txt-to-qti --validate questions.txt         # Validate only

For more information, visit: https://github.com/yourusername/txt-to-qti
        """
    )
    
    parser.add_argument('--version', action='version', version=f'txt-to-qti {__version__}')
    
    # Input files
    parser.add_argument('files', nargs='*', help='Input text files to convert')
    
    # Output options
    parser.add_argument('-o', '--output', 
                       help='Output QTI ZIP file (for single file only)')
    parser.add_argument('--base-name', 
                       help='Base name for generated files')
    
    # Conversion modes
    parser.add_argument('--smart', action='store_true', default=True,
                       help='Use smart conversion with change detection (default)')
    parser.add_argument('--classic', action='store_true',
                       help='Use classic conversion (always regenerate)')
    parser.add_argument('--force', action='store_true',
                       help='Force regeneration even if files are up to date')
    
    # Information modes
    parser.add_argument('--status', action='store_true',
                       help='Show file status without converting')
    parser.add_argument('--preview', action='store_true',
                       help='Preview conversion without creating output')
    parser.add_argument('--validate', action='store_true',
                       help='Validate questions only (no output)')
    
    # Batch processing
    parser.add_argument('--batch', action='store_true',
                       help='Process multiple files')
    
    # Validation options
    parser.add_argument('--no-validate', action='store_true',
                       help='Skip question validation')
    parser.add_argument('--strict', action='store_true',
                       help='Use strict validation (treat warnings as errors)')
    
    # Output options
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output')
    parser.add_argument('-q', '--quiet', action='store_true',
                       help='Quiet mode (minimal output)')
    
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main CLI entry point.
    
    Args:
        argv: Command line arguments (for testing)
        
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    
    # Validate arguments
    if not args.files and not args.status and not args.preview:
        parser.print_help()
        return 1
        
    if args.output and len(args.files) > 1:
        print("Error: --output can only be used with a single input file", file=sys.stderr)
        return 1
        
    if args.quiet and args.verbose:
        print("Error: --quiet and --verbose are mutually exclusive", file=sys.stderr)
        return 1
        
    # Set up converter
    validate_questions = not args.no_validate
    
    try:
        if args.smart and not args.classic:
            converter = SmartConverter(validate_questions=validate_questions)
            return handle_smart_conversion(converter, args)
        else:
            converter = TxtToQtiConverter(validate_questions=validate_questions)
            return handle_classic_conversion(converter, args)
            
    except TxtToQtiError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def handle_smart_conversion(converter: SmartConverter, args) -> int:
    """Handle smart conversion mode."""
    if args.batch or len(args.files) > 1:
        return handle_batch_conversion(converter, args)
        
    input_file = args.files[0] if args.files else None
    
    if args.status:
        return show_file_status(converter, input_file, args)
        
    if args.preview:
        return show_conversion_preview(converter, input_file, args)
        
    # Single file conversion
    try:
        qti_file, question_count, was_regenerated = converter.convert_with_intelligence(
            input_file,
            output_file=args.output,
            force=args.force,
            base_name=args.base_name
        )
        
        if not args.quiet:
            if was_regenerated:
                print(f"✓ Converted {question_count} questions")
                print(f"✓ QTI package: {Path(qti_file).name}")
            else:
                print(f"✓ Files up to date ({question_count} questions)")
                print(f"✓ QTI package: {Path(qti_file).name}")
                
            if args.verbose:
                status = converter.get_file_status(input_file, qti_file)
                print(f"  Input: {status['input_file']['formatted_time']}")
                print(f"  Output: {status['output_file']['formatted_time']}")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_classic_conversion(converter: TxtToQtiConverter, args) -> int:
    """Handle classic conversion mode."""
    if args.batch or len(args.files) > 1:
        # Batch classic conversion
        success_count = 0
        for input_file in args.files:
            try:
                if args.validate:
                    preview = converter.preview_conversion(input_file)
                    print(f"{input_file}: {'✓' if preview['success'] else '✗'} "
                          f"{preview.get('total_questions', 0)} questions")
                    if not preview['success']:
                        print(f"  Error: {preview.get('error', 'Unknown error')}")
                    continue
                    
                qti_file = converter.convert_file(
                    input_file,
                    base_name=args.base_name
                )
                
                question_count = len(converter.get_last_questions())
                
                if not args.quiet:
                    print(f"✓ {input_file}: {question_count} questions → {Path(qti_file).name}")
                    
                success_count += 1
                
            except Exception as e:
                print(f"✗ {input_file}: {e}", file=sys.stderr)
                
        if not args.quiet and not args.validate:
            print(f"\nProcessed {success_count}/{len(args.files)} files successfully")
            
        return 0 if success_count == len(args.files) else 1
        
    # Single file
    input_file = args.files[0]
    
    try:
        if args.validate or args.preview:
            preview = converter.preview_conversion(input_file)
            
            if not args.quiet:
                print(f"File: {input_file}")
                print(f"Questions: {preview.get('total_questions', 0)}")
                print(f"Valid: {'Yes' if preview['success'] else 'No'}")
                
                if not preview['success']:
                    print(f"Error: {preview.get('error', 'Unknown error')}")
                    
                if args.verbose and preview.get('validation_results'):
                    results = preview['validation_results']
                    if results['total_errors'] > 0:
                        print(f"Errors: {results['total_errors']}")
                        for error in results['errors'][:3]:
                            print(f"  - {error}")
                    if results['total_warnings'] > 0:
                        print(f"Warnings: {results['total_warnings']}")
                        
            return 0 if preview['success'] else 1
            
        # Regular conversion
        qti_file = converter.convert_file(
            input_file,
            output_file=args.output,
            base_name=args.base_name
        )
        
        question_count = len(converter.get_last_questions())
        
        if not args.quiet:
            print(f"✓ Converted {question_count} questions")
            print(f"✓ QTI package: {Path(qti_file).name}")
            
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_batch_conversion(converter: SmartConverter, args) -> int:
    """Handle batch smart conversion."""
    if args.preview:
        preview = converter.preview_batch_conversion(args.files)
        
        if not args.quiet:
            print(f"Batch preview: {len(args.files)} files")
            print(f"Would convert: {preview['would_convert']}")
            print(f"Would skip: {preview['would_skip']}")
            print(f"Invalid files: {preview['invalid_files']}")
            
            if args.verbose:
                for detail in preview['details']:
                    status_symbol = {'would_convert': '→', 'up_to_date': '✓', 'invalid': '✗'}
                    symbol = status_symbol.get(detail['status'], '?')
                    print(f"  {symbol} {detail['input_file']}")
                    
        return 0
        
    # Actual batch conversion
    results = converter.batch_convert(args.files, force=args.force)
    
    if not args.quiet:
        print(f"Batch conversion: {results['total_files']} files")
        print(f"Converted: {results['converted']}")
        print(f"Skipped (up to date): {results['skipped']}")
        print(f"Failed: {results['failed']}")
        
        if args.verbose:
            for detail in results['details']:
                status_symbols = {'converted': '✓', 'up_to_date': '=', 'failed': '✗'}
                symbol = status_symbols.get(detail['status'], '?')
                print(f"  {symbol} {detail['input_file']}")
                if detail['error']:
                    print(f"    Error: {detail['error']}")
                    
    return 0 if results['failed'] == 0 else 1


def show_file_status(converter: SmartConverter, input_file: str, args) -> int:
    """Show detailed file status."""
    try:
        status = converter.get_file_status(input_file)
        
        print(f"File Status: {input_file}")
        print("-" * 50)
        
        # Input file info
        inp = status['input_file']
        print(f"Input:  {inp['name']} ({'exists' if inp['exists'] else 'missing'})")
        if inp['exists']:
            print(f"        {inp['formatted_time']} ({inp['size']} bytes)")
            
        # Output file info
        out = status['output_file']
        print(f"Output: {out['name']} ({'exists' if out['exists'] else 'missing'})")
        if out['exists']:
            print(f"        {out['formatted_time']} ({out['size']} bytes)")
            
        # Status
        print(f"Status: {'Needs regeneration' if status['needs_regeneration'] else 'Up to date'}")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def show_conversion_preview(converter, input_file: str, args) -> int:
    """Show conversion preview."""
    try:
        base_converter = TxtToQtiConverter(validate_questions=True)
        preview = base_converter.preview_conversion(input_file)
        
        print(f"Conversion Preview: {input_file}")
        print("-" * 50)
        
        if preview['success']:
            print(f"✓ Valid: {preview['total_questions']} questions")
            print(f"Output: {Path(preview['estimated_output_file']).name}")
            
            if args.verbose:
                stats = preview['parsing_stats']
                print(f"Average options: {stats['average_options']}")
                print(f"Answer distribution: {stats['answer_distribution']}")
                
                if preview['answer_distribution_warnings']:
                    print("Warnings:")
                    for warning in preview['answer_distribution_warnings']:
                        print(f"  - {warning}")
        else:
            print(f"✗ Invalid: {preview['error']}")
            
        return 0 if preview['success'] else 1
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())