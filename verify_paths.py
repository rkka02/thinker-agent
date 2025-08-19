#!/usr/bin/env python3
"""
Verification script for thinker agent path references
Ensures all file references in .claude/commands/thinker.md point to existing files
"""

import os
import re
from pathlib import Path

def verify_agent_paths():
    """Verify that all path references in the agent file point to existing files"""
    base_dir = Path("/Users/mw/Desktop/thinker-agent")
    command_file = base_dir / ".claude/commands/thinker.md"
    
    print("Verifying Thinker Agent Path References")
    print("=" * 45)
    
    if not command_file.exists():
        print(f"❌ Command file not found: {command_file}")
        return False
        
    # Read the command file
    content = command_file.read_text()
    
    # Extract path references from the file
    path_patterns = [
        r'\.core/([^}]+)}',  # .core/{type}/{name} patterns
        r'\.core/([^`\s]+)',  # Direct .core/ path references
    ]
    
    referenced_paths = set()
    for pattern in path_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            # Clean up the match
            if match.endswith('/'):
                continue  # Skip directory references
            referenced_paths.add(f".core/{match}")
    
    # Add the core config file which is explicitly referenced
    referenced_paths.add(".core/core-config.yaml")
    
    print(f"\\n1. Found {len(referenced_paths)} path references in command file")
    
    # Check each referenced path
    missing_paths = []
    existing_paths = []
    
    for ref_path in sorted(referenced_paths):
        full_path = base_dir / ref_path
        if full_path.exists():
            existing_paths.append(ref_path)
            print(f"   ✓ {ref_path}")
        else:
            missing_paths.append(ref_path)
            print(f"   ✗ {ref_path} - MISSING")
    
    print(f"\\n2. Path Verification Summary:")
    print(f"   ✓ Found: {len(existing_paths)} files")
    print(f"   ✗ Missing: {len(missing_paths)} files")
    
    # Check for .bmad-core references (should not exist)
    bmad_refs = re.findall(r'\.bmad-core', content)
    if bmad_refs:
        print(f"\\n⚠️  WARNING: Found {len(bmad_refs)} .bmad-core references (should be .core)")
    else:
        print(f"\\n✓ No .bmad-core references found (good!)")
        
    # Check that core/{type} references are .core/{type}
    core_refs = re.findall(r'[^.]core/', content)
    if core_refs:
        print(f"\\n⚠️  WARNING: Found {len(core_refs)} core/ references (should be .core/)")
    else:
        print(f"\\n✓ All core references properly prefixed with '.' (good!)")
    
    print("\\n" + "=" * 45)
    if not missing_paths and not bmad_refs and not core_refs:
        print("🎉 ALL PATH REFERENCES VERIFIED!")
        print("The /thinker command should work correctly.")
        return True
    else:
        print("❌ PATH REFERENCE ISSUES FOUND!")
        if missing_paths:
            print(f"Missing files: {missing_paths}")
        return False

if __name__ == "__main__":
    success = verify_agent_paths()
    exit(0 if success else 1)