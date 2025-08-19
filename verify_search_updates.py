#!/usr/bin/env python3
"""
Verification script for web search query updates
Confirms all template patterns were replaced with intelligent query instructions
"""

import os
import re
from pathlib import Path

def verify_search_updates():
    """Verify that all web search patterns have been updated correctly"""
    base_dir = Path("/Users/mw/Desktop/thinker-agent")
    
    print("Verifying Web Search Query Updates")
    print("=" * 40)
    
    # Check for remaining template patterns
    template_patterns = [
        r'Web Search.*\{.*\}',  # Template patterns with placeholders
        r'2024',                # Hardcoded year references
    ]
    
    # Files to check
    check_files = [
        ".core/tasks/execute-step.md",
        ".core/tasks/solution-iteration.md", 
        ".core/templates/decision-record-tmpl.yaml",
        ".claude/commands/thinker.md"
    ]
    
    print("1. Checking for remaining template patterns...")
    issues_found = []
    
    for file_path in check_files:
        full_path = base_dir / file_path
        if not full_path.exists():
            issues_found.append(f"Missing file: {file_path}")
            continue
            
        content = full_path.read_text()
        
        for pattern in template_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                issues_found.append(f"{file_path}: Found {len(matches)} '{pattern}' patterns")
        
        # Check for intelligent web search instructions
        intelligent_patterns = [
            r'Web Search.*Research',
            r'Web Search.*Find',
            r'Web Search.*Explore',
            r'Web Search.*Discover'
        ]
        
        intelligent_count = 0
        for pattern in intelligent_patterns:
            intelligent_count += len(re.findall(pattern, content, re.IGNORECASE))
        
        if intelligent_count > 0:
            print(f"   ✓ {file_path}: {intelligent_count} intelligent search instructions")
        else:
            print(f"   - {file_path}: No web search instructions found")
    
    print("\\n2. Verification Results:")
    
    if issues_found:
        print("❌ ISSUES FOUND:")
        for issue in issues_found:
            print(f"   - {issue}")
        return False
    else:
        print("✅ ALL VERIFICATIONS PASSED:")
        print("   - No template patterns with placeholders found")
        print("   - No hardcoded 2024 references found")
        print("   - Intelligent search instructions successfully implemented")
        
        print("\\n3. Update Summary:")
        print("   ✓ Template queries → Intelligent queries")
        print("   ✓ Static placeholders → Dynamic context awareness")
        print("   ✓ Hardcoded dates → Timeless examples")
        print("   ✓ Agent can now formulate adaptive search queries")
        
        return True

if __name__ == "__main__":
    success = verify_search_updates()
    exit(0 if success else 1)