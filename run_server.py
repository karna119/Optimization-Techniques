#!/usr/bin/env python3
"""
Simple HTTP Server to view the Engineering Optimization Study Guide
Run this script and open http://localhost:8000 in your browser
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Change to the study guide directory
os.chdir(r"c:\Users\swathikaran\Downloads\study_guide_export (1)")

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

print("=" * 60)
print("Engineering Optimization Study Guide Server")
print("=" * 60)
print(f"\n✅ Starting server on http://localhost:{PORT}")
print(f"\n📂 Serving files from: {os.getcwd()}\n")
print("Press Ctrl+C to stop the server\n")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Server is running! Open your browser and visit:")
        print(f"   👉 http://localhost:{PORT}\n")
        
        # Try to open browser automatically
        try:
            webbrowser.open(f"http://localhost:{PORT}")
            print("📱 Browser window should open automatically...\n")
        except:
            pass
        
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n❌ Server stopped by user")
except Exception as e:
    print(f"\n❌ Error: {e}")
