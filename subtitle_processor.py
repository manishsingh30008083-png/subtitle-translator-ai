# Subtitle Processor

This script handles the parsing and processing of SRT and VTT subtitle formats.

## Requirements
- Python 3.x

## Functions

### parse_srt(file_path)
Parses an SRT file and returns a list of subtitle entries.

### parse_vtt(file_path)
Parses a VTT file and returns a list of subtitle entries.

### process_subtitles(subtitle_entries)
Processes the subtitle entries and applies any required transformations.

## Example Usage
if __name__ == '__main__':
    srt_entries = parse_srt('example.srt')
    vtt_entries = parse_vtt('example.vtt')
    processed_entries = process_subtitles(srt_entries)
    
    for entry in processed_entries:
        print(entry)