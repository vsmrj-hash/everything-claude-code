#!/usr/bin/env python3
"""Upload all 7 resume templates to the Google Drive 'Resumes' folder."""

import base64
import json
import os
import time
import requests

# MCP endpoint and session credentials
SESSION_ID = "cse_01KZ8FVKsSSD4ZKyii55cy1H"
MCP_URL = (
    f"https://api.anthropic.com/v2/ccr-sessions/{SESSION_ID}/mcp"
    "?mcp_url=https%3A%2F%2Fdrivemcp.googleapis.com%2Fmcp%2Fv1"
    "&mcp_server_id=c19beafa-130a-598f-90fb-9636bfe4b17a"
    "&toolbox_mcp_server_id=0debe23d-e7bc-4d16-b2a7-d7979d5c325d"
)
INGRESS_TOKEN_FILE = "/home/claude/.claude/remote/.session_ingress_token"
DRIVE_FOLDER_ID = "1N4_g_x3siE6Q9YV4sfDIwWExwa3aytHW"
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

TEMPLATES_DIR = os.path.dirname(os.path.abspath(__file__))
FILES = [
    "01_USA_Resume_ATS_Optimized.docx",
    "02_UK_CV_Professional.docx",
    "03_EU_Europass_CV.docx",
    "04_Japan_Resume_Rirekisho_Style.docx",
    "05_India_Resume_Professional.docx",
    "06_Australia_Resume_Professional.docx",
    "07_NewZealand_CV_Professional.docx",
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
                "contentMimeType": DOCX_MIME,
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
        # Show only first 500 chars of response to avoid flooding output
        print(f"  Response: {response[:500]}")

        if status != 200:
            print(f"  ERROR - retrying in 3s...")
            time.sleep(3)
            status, response = mcp_create_file(token, filename, b64, DRIVE_FOLDER_ID)
            print(f"  Retry HTTP status: {status}")
            print(f"  Retry Response: {response[:500]}")

        time.sleep(1)  # rate-limit courtesy delay

    print("\nDone!")


if __name__ == "__main__":
    main()
