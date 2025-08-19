# Thinker Agent - Problem Solver Iterative

Universal problem-solving agent with systematic iterative thinking capabilities, migrated to standalone architecture.

## Overview

This is a complete migration of the problem-solver-iterative agent, designed for systematic analysis across any domain - scientific research, philosophical inquiry, personal decisions, creative projects, academic investigation, mathematical problems, artistic challenges, and life decisions.

## Features

- **Universal Iterative Thinking**: Step-by-step progression with validation gates
- **Complexity-Adaptive Depth**: Matches analytical rigor to problem complexity  
- **Cross-Domain Intelligence**: Applies frameworks across disciplines
- **Systematic Methodology**: 15+ problem-solving frameworks integrated
- **Progressive Learning**: Captures insights and builds understanding iteratively

## Agent Commands

- `*think` - Universal thinking orchestrator with adaptive planning (3/5/7/10 steps)
- `*solve` - Progressive solution evolution through multiple cycles  
- `*status` - Session tracking and progress monitoring
- `*help` - Context-aware assistance

## Quick Start

1. **Load the agent**: Use the command `/thinker` or load `.core/agents/thinker.md`
2. **For Systematic Analysis**: Use `*think` with your problem
3. **For Solution Generation**: Use `*solve` with your challenge
4. **Check Progress**: Use `*status` anytime
5. **Get Help**: Use `*help` for guidance

## Universal Applications

- **🔬 Scientific Research**: Hypothesis development, experimental design, theory building
- **🤔 Philosophical Inquiry**: Conceptual analysis, argument construction, ethical reasoning
- **🎯 Personal Decisions**: Life choices, goal setting, relationship decisions, career planning
- **🎨 Creative Projects**: Artistic development, design challenges, innovation breakthroughs
- **📚 Academic Investigation**: Research problems, thesis development, scholarly analysis
- **📐 Mathematical Problems**: Proof development, problem-solving strategies
- **🎭 Artistic Challenges**: Creative expression, aesthetic decisions, artistic vision
- **🌱 Life Decisions**: Personal growth, value clarification, major life transitions

## Key Features

### Thinking Framework (UCAIT)
- **Complexity Assessment**: Automatically determines optimal thinking depth
- **Multi-Layer Analysis**: 5 cognitive layers applied simultaneously
- **Real-Time Research**: Integrates current knowledge from web research
- **Universal Validation**: Applies appropriate standards for any domain

### Solution Framework (USGS)  
- **Systematic Generation**: Multiple proven methodologies applied in sequence
- **Progressive Refinement**: Each cycle improves solution quality
- **Cross-Domain Innovation**: Applies insights from multiple fields
- **Universal Categories**: Solution types that work across all domains

## Directory Structure

```
.core/
├── agents/
│   └── thinker.md                      # Main agent file
├── tasks/                              # Problem-solving task implementations
│   ├── complexity-assessment.md
│   ├── create-thinking-plan.md
│   ├── execute-step.md
│   └── [12 more task files]
├── templates/                          # Interactive document templates  
│   ├── complexity-assessment-tmpl.yaml
│   ├── thinking-plan-tmpl.yaml
│   └── [5 more template files]
├── checklists/                         # Quality assurance checklists
│   ├── problem-solver-checklist.md
│   └── [2 more checklist files]
├── data/                              # Knowledge libraries and guides
│   ├── problem-solving-methods.md
│   ├── mental-models-library.md
│   └── [2 more data files]
├── utils/                             # Supporting utilities
│   ├── complexity-assessor.md
│   └── [2 more utility files]
└── core-config.yaml                   # Core configuration
```

## Simple Usage Examples

**Thinking Example**:
```
You: "/thinker"
Thinker: "Hello! I'm your Universal Cognitive Assistant..."
You: "*think How should I approach my PhD research topic selection?"
Thinker: "5-step thinking plan generated. Execute automatically? Yes/No/Adjust"
You: "Yes"
Thinker: [Executes 5 thinking steps with cross-domain research and insights]
```

**Solution Example**:
```
You: "*solve I need to design a better morning routine"
Thinker: "3-cycle solution evolution planned. Execute? Yes/No/Adjust"
You: "Yes" 
Thinker: [Generates, refines, and optimizes solutions using multiple methodologies]
```

## Why Universal?

- **Domain-Agnostic**: Same powerful frameworks work for any field
- **Fine-Tunable**: Automatically adapts to your specific domain
- **Cross-Pollination**: Discovers insights by connecting across fields
- **Proven Methodologies**: Built on time-tested universal frameworks (Polya, CPS, Synectics, etc.)
- **Research-Enhanced**: Real-time integration of current knowledge and best practices

## Problem Complexity Levels
- **Simple (3 steps)**: Single domain, clear stakeholders, known solutions
- **Medium (5 steps)**: Multiple domains, some conflicts, adaptation needed  
- **Complex (7 steps)**: Cross-disciplinary, competing stakeholders, innovation required
- **Wicked (10 steps)**: Novel domains, unknown stakeholders, breakthrough needed

## Testing

Run the included test script to verify migration integrity:

```bash
python test_agent.py
```

## Key Principles

- **First Principles Thinking**: Decompose to fundamental truths
- **Systems Perspective**: Identify leverage points and patterns
- **Iterative Discipline**: Step-by-step progression with validation
- **Cross-Domain Synthesis**: Create insights transcending boundaries
- **Progressive Learning**: Build understanding systematically

## Migration Notes

This agent has been successfully migrated from the BMad framework to a standalone structure:
- All dependencies properly copied and created
- File references updated from `.bmad-core/` to `.core/`
- All 33 required files verified and accessible
- Agent functionality preserved and tested

Transform any challenge into systematic progress with the power of universal cognitive frameworks! 🧠✨