#!/usr/bin/env python3
"""Upload all 7 Manish personalised PDFs to the Google Drive 'Resumes' folder."""

import base64
import os
import time
import requests

SESSION_ID = "cse_01KZ8FVKsSSD4ZKyii55cy1H"
MCP_URL = (
    f"https://api.anthropic.com/v2/ccr-sessions/{SESSION_ID}/mcp"
    "?mcp_url=https%3A%2F%2Fdrivemcp.googleapis.com%2Fmcp%2Fv1"
    "&mcp_server_id=c19beafa-130a-598f-90fb-9636bfe4b17a"
    "&toolbox_mcp_server_id=0debe23d-e7bc-4d16-b2a7-d7979d5c325d"
)
INGRESS_TOKEN_FILE = "/home/claude/.claude/remote/.session_ingress_token"
DRIVE_FOLDER_ID = "1N4_g_x3siE6Q9YV4sfDIwWExwa3aytHW"
PDF_MIME = "application/pdf"

TEMPLATES_DIR = os.path.dirname(os.path.abspath(__file__))
FILES = [
    "01_Manish_USA_Resume.pdf",
    "02_Manish_UK_CV.pdf",
    "03_Manish_EU_Europass_CV.pdf",
    "04_Manish_Japan_Resume.pdf",
    "05_Manish_India_CV.pdf",
    "06_Manish_Australia_Resume.pdf",
    "07_Manish_NewZealand_CV.pdf",
]


def get_token():
    with open(INGRESS_TOKEN_FILE) as f:
        return f.read().strip()


def mcp_create_file(token, title, b64content, parent_id):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Session-UUID": SESSION_ID,
        "X-MCP-Server-ID": "0debe23d-e7bc-4d16-b2a7-d7979d5c325d",
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": "create_file",
            "arguments": {
                "title": title,
                "base64Content": b64content,
                "contentMimeType": PDF_MIME,
                "disableConversionToGoogleType": True,
                "parentId": parent_id,
            },
        },
    }
    resp = requests.post(MCP_URL, headers=headers, json=payload, timeout=60)
    return resp.status_code, resp.text


def main():
    token = get_token()
    print(f"Token length: {len(token)}")

    for filename in FILES:
        filepath = os.path.join(TEMPLATES_DIR, filename)
        print(f"\nUploading {filename}...")
        with open(filepath, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("ascii")
        print(f"  File size: {len(data)} bytes, base64 length: {len(b64)} chars")

        status, response = mcp_create_file(token, filename, b64, DRIVE_FOLDER_ID)
        print(f"  HTTP status: {status}")
        print(f"  Response: {response[:500]}")

        if status != 200:
            print(f"  ERROR - retrying in 3s...")
            time.sleep(3)
            status, response = mcp_create_file(token, filename, b64, DRIVE_FOLDER_ID)
            print(f"  Retry HTTP status: {status}")
            print(f"  Retry Response: {response[:500]}")

        time.sleep(1)

    print("\nDone!")


if __name__ == "__main__":
    main()
