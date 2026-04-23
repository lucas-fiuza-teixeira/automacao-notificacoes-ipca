from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def aplicar_bordas(tabela):
    tbl = tabela._element
    borders = OxmlElement('w:tblBorders')

    for b in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{b}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '8')
        border.set(qn('w:color'), '000000')
        borders.append(border)

    tbl.tblPr.append(borders)