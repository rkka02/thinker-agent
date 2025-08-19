#!/usr/bin/env python3
"""
Test script for thinker agent migration
Verifies all components are properly migrated and accessible
"""

import os
import sys
from pathlib import Path

def test_agent_migration():
    """Test that all required files exist and are accessible"""
    base_dir = Path("/Users/mw/Desktop/thinker-agent/.core")
    
    # Required directory structure
    required_dirs = [
        "agents", "tasks", "templates", "checklists", "data", "utils"
    ]
    
    # Required files
    required_files = {
        "agents/thinker.md": "Main agent file",
        "core-config.yaml": "Core configuration",
        
        # Task files
        "tasks/complexity-assessment.md": "Complexity assessment task",
        "tasks/create-thinking-plan.md": "Thinking plan creation",
        "tasks/execute-step.md": "Step execution",
        "tasks/plan-status.md": "Plan status tracking",
        "tasks/thinking-synthesis.md": "Insight synthesis",
        "tasks/solution-iteration.md": "Solution iteration",
        
        # Template files  
        "templates/complexity-assessment-tmpl.yaml": "Complexity assessment template",
        "templates/thinking-plan-tmpl.yaml": "Thinking plan template",
        "templates/step-execution-tmpl.yaml": "Step execution template",
        
        # Checklist files
        "checklists/problem-solver-checklist.md": "Problem solver checklist",
        "checklists/iterative-thinking-checklist.md": "Iterative thinking checklist",
        
        # Data files
        "data/problem-solving-methods.md": "Problem solving methods library",
        "data/mental-models-library.md": "Mental models library",
        "data/complexity-assessment-guide.md": "Complexity assessment guide",
        
        # Utils files
        "utils/complexity-assessor.md": "Complexity assessor utility",
        "utils/method-selector.md": "Method selector utility",
        "utils/step-validator.md": "Step validator utility"
    }
    
    print("Testing Problem-Solver-Iterative Agent Migration")
    print("=" * 50)
    
    # Test directory structure
    print("\\n1. Testing directory structure...")
    missing_dirs = []
    for dir_name in required_dirs:
        dir_path = base_dir / dir_name
        if dir_path.exists() and dir_path.is_dir():
            print(f"   ✓ {dir_name}/")
        else:
            print(f"   ✗ {dir_name}/ - MISSING")
            missing_dirs.append(dir_name)
    
    # Test required files
    print("\\n2. Testing required files...")
    missing_files = []
    for file_path, description in required_files.items():
        full_path = base_dir / file_path
        if full_path.exists() and full_path.is_file():
            print(f"   ✓ {file_path}")
        else:
            print(f"   ✗ {file_path} - MISSING ({description})")
            missing_files.append(file_path)
    
    # Test agent file content
    print("\\n3. Testing agent file integrity...")
    agent_file = base_dir / "agents/thinker.md"
    if agent_file.exists():
        content = agent_file.read_text()
        
        # Check for key components
        checks = [
            ("ACTIVATION-NOTICE", "Activation notice present"),
            ("YAML block", "```yaml" in content and "```" in content),
            (".core/ references", ".core/" in content and ".bmad-core/" not in content),
            ("Agent commands", "commands:" in content),
            ("Dependencies", "dependencies:" in content),
            ("Iterative thinking", "iterative_thinking_behavior:" in content)
        ]
        
        for check_name, condition in checks:
            if isinstance(condition, str):
                result = condition in content
            else:
                result = condition
                
            if result:
                print(f"   ✓ {check_name}")
            else:
                print(f"   ✗ {check_name} - MISSING/INCORRECT")
    
    # Summary
    print("\\n" + "=" * 50)
    if not missing_dirs and not missing_files:
        print("🎉 MIGRATION SUCCESSFUL!")
        print("All required components are present and accessible.")
        print("\\nThe agent should be fully functional at:")
        print(f"   {base_dir}/agents/thinker.md")
        return True
    else:
        print("❌ MIGRATION INCOMPLETE!")
        if missing_dirs:
            print(f"Missing directories: {', '.join(missing_dirs)}")
        if missing_files:
            print(f"Missing files: {', '.join(missing_files)}")
        return False

if __name__ == "__main__":
    success = test_agent_migration()
    sys.exit(0 if success else 1)