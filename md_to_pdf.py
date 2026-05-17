import markdown
from weasyprint import HTML
import os

def convert_md_to_pdf(input_md_path, output_pdf_path):
    """
    Converts a Markdown file to a PDF file.
    """
    # 1. Verify the input file exists
    if not os.path.exists(input_md_path):
        print(f"Error: The file '{input_md_path}' was not found.")
        return

    # 2. Read the Markdown file
    with open(input_md_path, 'r', encoding='utf-8') as md_file:
        md_text = md_file.read()

    # 3. Convert Markdown to HTML
    # We use 'extra' for tables, footnotes, etc., and 'codehilite' for code blocks
    html_content = markdown.markdown(
        md_text, 
        extensions=['extra', 'codehilite', 'toc']
    )

    # Wrap the HTML with basic styling to ensure the PDF looks good
    styled_html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 40px;
                color: #333;
            }}
            h1, h2, h3 {{
                color: #222;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
                font-family: monospace;
            }}
            pre code {{
                display: block;
                padding: 10px;
                overflow-x: auto;
            }}
            blockquote {{
                border-left: 4px solid #ccc;
                margin-left: 0;
                padding-left: 16px;
                color: #666;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # 4. Convert the styled HTML to PDF using WeasyPrint
    print(f"Converting '{input_md_path}' to '{output_pdf_path}'...")
    HTML(string=styled_html).write_pdf(output_pdf_path)
    print("Conversion complete!")

if __name__ == "__main__":
    # Replace these with your actual file names
    INPUT_MARKDOWN = "README.md"
    OUTPUT_PDF = "README.pdf"
    
    convert_md_to_pdf(INPUT_MARKDOWN, OUTPUT_PDF)