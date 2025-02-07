import fitz  # PyMuPDF
from typing import List, Dict, Any

def append_group(groups, font_size, group_text, group_positions, page_number):
    if group_text:
        groups.append({
            "font_size": font_size,
            "group_text": " ".join(group_text),
            "positions": group_positions,
            "page_number": page_number
        })

def process_text_block(block, previous_font_size: float, current_group: List[str],
                       group_positions: List[Any], groups: List[Dict[str, Any]], page_number: int,
                       font_size_tolerance: float = 0.5, distance_threshold: float = 80.0):
    for line in block.get('lines', []):
        for span in line.get('spans', []):
            font_size = span.get('size')
            text = span.get('text', '').strip()
            bbox = span.get('bbox')

            if not text:
                continue

            if group_positions:
                last_bbox = group_positions[-1]
                horizontal_distance = abs(bbox[0] - last_bbox[2])

                if horizontal_distance > distance_threshold or abs(font_size - previous_font_size) > font_size_tolerance:
                    append_group(groups, previous_font_size, current_group, group_positions, page_number)
                    current_group = []
                    group_positions = []

            current_group.append(text)
            group_positions.append(bbox)
            previous_font_size = font_size

    return previous_font_size, current_group, group_positions