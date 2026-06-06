import zipfile
import xml.etree.ElementTree as ET

def inspect_images(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        # Read relations
        rels_xml = z.read('word/_rels/document.xml.rels')
        rels_root = ET.fromstring(rels_xml)
        
        # Map rId to target image file
        rel_map = {}
        # The document.xml.rels uses Relationship elements
        # They usually have no namespace prefixes in their local names but are inside a namespace.
        # Let's extract Relationship tags using a namespace-agnostic search or standard namespaces.
        for rel in rels_root.findall('.//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            rid = rel.get('Id')
            target = rel.get('Target')
            rel_map[rid] = target
        if not rel_map:
            # Fallback if the namespace is different or empty
            for rel in rels_root.findall('.//Relationship'):
                rid = rel.get('Id')
                target = rel.get('Target')
                rel_map[rid] = target

        # Read document XML
        doc_xml = z.read('word/document.xml')
        doc_root = ET.fromstring(doc_xml)
        
        # XML Namespaces
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
            'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
            'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
        }

        # Iterate paragraphs and find drawings
        for p_idx, p in enumerate(doc_root.findall('.//w:p', namespaces)):
            # Get text of paragraph
            texts = [t.text for t in p.findall('.//w:t', namespaces) if t.text]
            p_text = ''.join(texts).strip()
            
            # Find drawings/images embedded in this paragraph
            drawings = p.findall('.//w:drawing', namespaces)
            if drawings:
                for drawing in drawings:
                    blips = drawing.findall('.//a:blip', namespaces)
                    for blip in blips:
                        embed_id = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                        image_path = rel_map.get(embed_id, 'Unknown')
                        print(f"Paragraph {p_idx:03d} | Text: '{p_text:.60s}...' | Image: {image_path} (embed ID: {embed_id})")

if __name__ == '__main__':
    inspect_images('Solemne 2 - Cálculo(forma A).docx')
