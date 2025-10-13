#!/usr/bin/env python3
"""Bulk GitHub Issue Creator for AML Risk Assessment Tool"""

import os
import sys
from github import Github

# Issue definitions
ISSUES = [
    {
        "title": "Download and Review GC 2023 Guidance",
        "body": """**Estimate:** 2 hours (AI-assisted summary and analysis)

## Description
Download and thoroughly review the full Gambling Commission 2023 ML/TF Risk Assessment guidance document.

## Tasks
- [ ] Download PDF from GC website
- [ ] Use AI to extract and summarize key sections
- [ ] Review AI summary and validate accuracy
- [ ] Highlight sections relevant to each sector
- [ ] Note any sector-specific guidance
- [ ] Document structure and organization of risks

## AI Assistance
- PDF text extraction and summarization
- Key section identification
- Structure analysis

## Acceptance Criteria
- Complete document downloaded and saved
- AI-generated summary reviewed and validated
- Key sections identified for extraction""",
        "labels": ["content", "phase-1"],
        "milestone": "Content Preparation"
    },
    {
        "title": "Extract All Risks from GC Guidance",
        "body": """**Estimate:** 3-4 hours (AI-assisted extraction and structuring)

## Description
Extract all identified risks from the GC 2023 guidance document into a structured format.

## Tasks
- [ ] Create risk extraction template
- [ ] Use AI to extract risk titles and descriptions from PDF
- [ ] Review and validate AI extractions
- [ ] Assign unique Risk IDs
- [ ] Note page/section references
- [ ] Capture any risk-specific guidance

## AI Assistance
- Automated text extraction from PDF
- Pattern recognition for risk identification
- Initial structuring of data
- Cross-referencing and validation

## Acceptance Criteria
- All risks extracted into structured format
- Each risk has: ID, Title, Description, Source Reference
- Quality check completed (no missing risks)

## Dependencies
Issue #1""",
        "labels": ["content", "phase-1", "critical"],
        "milestone": "Content Preparation"
    },
    {
        "title": "Categorize Risks by Sector Applicability",
        "body": """**Estimate:** 2-3 hours (AI-assisted categorization)

## Description
Map each extracted risk to the applicable gambling sectors.

## Tasks
- [ ] Provide AI with risk list and sector definitions
- [ ] Use AI to suggest initial sector mappings
- [ ] Review and validate AI categorizations
- [ ] Create sector-to-risk mapping matrix
- [ ] Flag universal risks (apply to all sectors)
- [ ] Flag sector-specific risks
- [ ] Count risks per sector

## AI Assistance
- Pattern matching risks to sector characteristics
- Initial categorization suggestions
- Matrix generation

## Acceptance Criteria
- Complete mapping of risks to sectors
- Risk counts per sector documented
- Matrix validated for accuracy

## Dependencies
Issue #2""",
        "labels": ["content", "phase-1", "critical"],
        "milestone": "Content Preparation"
    },
    {
        "title": "Identify Simplest Low-Risk Sector for Demo",
        "body": """**Estimate:** 2 hours

## Description
Analyze Low-risk sectors to identify which has the fewest applicable risks for initial demo build.

## Tasks
- [ ] Compare risk counts for all Low-risk sectors:
  - Family Entertainment Centres (FECs)
  - Society lotteries and external lottery managers
  - The National Lottery
  - Gambling software
  - Gaming machine technical licences
- [ ] Consider complexity of risks (not just quantity)
- [ ] Document recommendation with rationale
- [ ] Get team approval on selected sector

## Acceptance Criteria
- Selected sector identified and documented
- Rationale clearly explained
- Team consensus achieved

## Dependencies
Issue #3""",
        "labels": ["content", "phase-1", "planning"],
        "milestone": "Content Preparation"
    },
    {
        "title": "Create Risk Library Spreadsheet",
        "body": """**Estimate:** 2 hours (AI-assisted data structuring)

## Description
Create master risk library in structured spreadsheet format.

## Tasks
- [ ] Design spreadsheet schema
- [ ] Required columns: Risk ID, Risk Title, Risk Description, Applicable Sectors, Source Reference
- [ ] Optional columns: Risk Category, Sub-category, Examples
- [ ] Use AI to populate spreadsheet from extracted data
- [ ] Validate data completeness
- [ ] Export as CSV for version control

## AI Assistance
- Automated spreadsheet population
- Data formatting and validation
- CSV generation

## Acceptance Criteria
- Complete risk library spreadsheet created
- All required fields populated
- Data validated
- CSV version committed to repo

## Dependencies
Issues #2, #3""",
        "labels": ["content", "phase-1", "deliverable"],
        "milestone": "Content Preparation"
    },
    {
        "title": "Review and Test Core Functionality Questions",
        "body": """**Estimate:** 3-4 hours (AI-assisted scenario generation and testing)

## Description
Review the proposed 4-option question structure and test with various scenarios.

## Tasks
- [ ] Document current question structure
- [ ] Use AI to generate 20+ test scenarios covering different risk types
- [ ] Test each scenario against question options
- [ ] Identify any scenarios not covered by current options
- [ ] Document edge cases
- [ ] Consider alternative phrasings

## AI Assistance
- Scenario generation covering edge cases
- Logical testing of question structure
- Alternative phrasing suggestions

## Acceptance Criteria
- Test scenarios documented
- Question structure validated or refinements proposed
- Edge cases identified and addressed
- Documentation updated in `/docs/question-design.md`""",
        "labels": ["design", "phase-2", "critical"],
        "milestone": "Question Design"
    },
    {
        "title": "Refine Question Wording and Create Help Text",
        "body": """**Estimate:** 2 hours (AI-assisted content generation)

## Description
Polish question wording for clarity and create guidance notes.

## Tasks
- [ ] Use AI to draft multiple question wording variations
- [ ] Select best wording for clarity
- [ ] Use AI to generate help text for main question
- [ ] Generate help text for each response option
- [ ] Create examples for each option
- [ ] Test readability (aim for clear, jargon-free language)
- [ ] Get feedback from potential user

## AI Assistance
- Multiple wording variations
- Help text generation
- Example creation
- Readability optimization

## Acceptance Criteria
- Final question wording documented
- Help text created for all elements
- Examples provided
- User feedback incorporated

## Dependencies
Issue #6""",
        "labels": ["design", "phase-2", "documentation"],
        "milestone": "Question Design"
    },
    {
        "title": "Test Conditional Logic Flow",
        "body": """**Estimate:** 1.5 hours (AI-assisted flowchart and logic validation)

## Description
Map out and test the conditional logic for question flow.

## Tasks
- [ ] Use AI to generate flowchart of conditional logic
- [ ] Document rules for each response path
- [ ] Test all possible response combinations
- [ ] Identify any circular logic or dead ends
- [ ] Document in `/docs/user-flow.md`

## AI Assistance
- Flowchart generation
- Logic path testing
- Dead end identification

## Acceptance Criteria
- Complete flowchart created
- All paths tested
- Logic rules documented
- No circular logic or dead ends

## Dependencies
Issue #6""",
        "labels": ["design", "phase-2", "technical"],
        "milestone": "Question Design"
    },
    {
        "title": "Extract Sample Risks for Demo Sector",
        "body": """**Estimate:** 2 hours

## Description
Extract 5-10 most relevant risks for the chosen demo sector.

## Tasks
- [ ] Filter risk library for selected sector
- [ ] Select 5-10 representative risks covering:
  - Different risk types
  - Different levels of complexity
  - Mix of common and sector-specific risks
- [ ] Create sample risk subset file
- [ ] Document selection rationale

## Acceptance Criteria
- 5-10 risks selected
- Sample risk file created
- Selection covers diverse risk types
- Rationale documented

## Dependencies
Issues #4, #5""",
        "labels": ["content", "phase-2", "demo"],
        "milestone": "Sample Build"
    },
    {
        "title": "Build Simple Prototype",
        "body": """**Estimate:** 6-8 hours (AI-assisted code generation)

## Description
Build functional prototype using selected sector and sample risks.

## Tasks
- [ ] Choose prototyping approach (HTML/React/other)
- [ ] Use AI to generate initial codebase structure
- [ ] Implement sector selection (single sector for demo)
- [ ] Implement risk questionnaire with conditional logic
- [ ] Implement free-text input fields
- [ ] Add basic progress tracking
- [ ] Add save functionality (local storage for demo)
- [ ] Implement basic navigation
- [ ] Test all user paths

## AI Assistance
- Initial code scaffolding
- Component generation
- Logic implementation
- Debugging support

## Acceptance Criteria
- Functional prototype deployed/runnable
- All core features working
- User can complete full assessment
- Data captured correctly

## Dependencies
Issues #7, #8, #9""",
        "labels": ["development", "phase-2", "demo", "critical", "ai-assisted"],
        "milestone": "Sample Build"
    },
    {
        "title": "Create Sample Outputs Using Test Data",
        "body": """**Estimate:** 4 hours (AI-assisted output generation)

## Description
Generate sample risk assessment report and policy action list outputs.

## Tasks
- [ ] Complete demo assessment with realistic test data
- [ ] Use AI to generate risk assessment report output
- [ ] Use AI to generate AML policy action list output
- [ ] Review outputs for completeness
- [ ] Refine as needed
- [ ] Save sample outputs to `/sample-build/sample-outputs/`

## AI Assistance
- Report formatting and generation
- Policy action item generation
- Professional document styling

## Acceptance Criteria
- Sample risk assessment report created
- Sample AML policy action list created
- Outputs demonstrate all features
- Quality validated by team

## Dependencies
Issue #10""",
        "labels": ["development", "phase-2", "demo", "ai-assisted"],
        "milestone": "Sample Build"
    },
    {
        "title": "Design Risk Assessment Report Structure",
        "body": """**Estimate:** 3 hours (AI-assisted design and mockup)

## Description
Design comprehensive structure and format for risk assessment report.

## Tasks
- [ ] Define report sections and order
- [ ] Design layout for each risk presentation
- [ ] Include: header, footer, table of contents
- [ ] Define formatting standards
- [ ] Use AI to create visual mockup/template
- [ ] Document in `/docs/output-templates.md`

## AI Assistance
- Report structure suggestions
- Professional formatting standards
- Mockup generation
- Template creation

## Acceptance Criteria
- Complete report structure documented
- Visual mockup created
- Format meets professional standards
- Appropriate for regulatory review

## Dependencies
Issue #6""",
        "labels": ["design", "phase-3", "deliverable", "ai-assisted"],
        "milestone": "Output Templates"
    },
    {
        "title": "Design AML Policy Action List Format",
        "body": """**Estimate:** 2 hours (AI-assisted design)

## Description
Design format and structure for AML policy action list.

## Tasks
- [ ] Define action list categories
- [ ] Design item format (what information to include)
- [ ] Determine prioritization/grouping logic
- [ ] Use AI to create visual mockup
- [ ] Document in `/docs/output-templates.md`

## AI Assistance
- Structure recommendations
- Categorization logic
- Mockup generation

## Acceptance Criteria
- Action list structure documented
- Format provides clear, actionable guidance
- Prioritization logic defined
- Mockup created

## Dependencies
Issue #6""",
        "labels": ["design", "phase-3", "deliverable", "ai-assisted"],
        "milestone": "Output Templates"
    },
    {
        "title": "Map Response Types to Policy Requirements",
        "body": """**Estimate:** 3 hours (AI-assisted mapping logic)

## Description
Define logic for auto-generating policy action items from different response types.

## Tasks
- [ ] Map each response option to policy implications
- [ ] Use AI to generate action item templates for each scenario
- [ ] Consider risk rating in policy recommendations
- [ ] Create mapping rules documentation
- [ ] Include examples for each mapping
- [ ] Document in `/docs/output-templates.md`

## AI Assistance
- Mapping logic development
- Template generation
- Example creation

## Acceptance Criteria
- Complete mapping rules documented
- Templates for each response type created
- Logic handles all scenarios
- Examples provided

## Dependencies
Issues #7, #13""",
        "labels": ["design", "phase-3", "critical", "ai-assisted"],
        "milestone": "Output Templates"
    },
    {
        "title": "Implement Output Generation Logic",
        "body": """**Estimate:** 6-8 hours (AI-assisted code generation)

## Description
Implement the logic to generate both output documents from assessment data.

## Tasks
- [ ] Use AI to generate risk assessment report generator code
- [ ] Use AI to generate policy action list generator code
- [ ] Apply formatting and styling
- [ ] Implement PDF export functionality
- [ ] Test with various data scenarios
- [ ] Handle edge cases (no data, partial data, etc.)

## AI Assistance
- Code generation for report logic
- PDF generation implementation
- Formatting and styling
- Edge case handling

## Acceptance Criteria
- Both outputs generated correctly
- PDF export working
- All formatting applied
- Edge cases handled gracefully

## Dependencies
Issues #12, #13, #14""",
        "labels": ["development", "phase-3", "critical", "ai-assisted"],
        "milestone": "Output Templates"
    },
    {
        "title": "Create Technical Specification",
        "body": """**Estimate:** 2 hours (AI-assisted documentation)

## Description
Document technical requirements and architecture decisions.

## Tasks
- [ ] Define data structure for risks and responses
- [ ] Document conditional logic rules
- [ ] Specify save/resume functionality
- [ ] Define security requirements
- [ ] Choose tech stack
- [ ] Use AI to draft REQUIREMENTS.md

## AI Assistance
- Documentation generation
- Best practices recommendations
- Architecture suggestions

## Acceptance Criteria
- Complete technical specification documented
- Architecture decisions explained
- Data models defined
- REQUIREMENTS.md created""",
        "labels": ["technical", "phase-4", "documentation", "ai-assisted"],
        "milestone": "Demo Development"
    },
    {
        "title": "Design UI/UX",
        "body": """**Estimate:** 4 hours (AI-assisted design)

## Description
Design user interface and user experience for demo.

## Tasks
- [ ] Use AI to create wireframes for all screens
- [ ] Design questionnaire interface
- [ ] Design progress indicator
- [ ] Design review/summary screen
- [ ] Consider accessibility requirements
- [ ] Get user feedback on designs

## AI Assistance
- Wireframe generation
- UI component suggestions
- Accessibility recommendations
- Design best practices

## Acceptance Criteria
- Complete wireframes created
- Design is clean and intuitive
- Accessibility considered
- User feedback incorporated""",
        "labels": ["design", "phase-4", "ai-assisted"],
        "milestone": "Demo Development"
    },
    {
        "title": "Implement Full Demo Application",
        "body": """**Estimate:** 10-12 hours (AI-assisted development)

## Description
Build complete demo application with all MVP features.

## Tasks
- [ ] Set up project structure
- [ ] Use AI to generate UI components based on designs
- [ ] Integrate risk library data
- [ ] Implement full questionnaire flow
- [ ] Implement progress tracking
- [ ] Implement save/resume functionality
- [ ] Integrate both output generators
- [ ] Add basic error handling
- [ ] Create deployment build

## AI Assistance
- Component code generation
- Integration logic
- Error handling implementation
- Deployment configuration

## Acceptance Criteria
- Fully functional demo application
- All MVP features implemented
- Professional UI
- Deployable/shareable demo

## Dependencies
Issues #16, #17, #15""",
        "labels": ["development", "phase-4", "critical", "ai-assisted"],
        "milestone": "Demo Development"
    },
    {
        "title": "End-to-End Testing",
        "body": """**Estimate:** 4 hours (AI-assisted test generation and execution)

## Description
Comprehensive testing of complete demo application.

## Tasks
- [ ] Use AI to generate test plan covering all features
- [ ] Test all user paths
- [ ] Test data persistence
- [ ] Test output generation
- [ ] Test edge cases
- [ ] Browser/device testing
- [ ] Document bugs found
- [ ] Fix critical bugs

## AI Assistance
- Test case generation
- Automated testing scripts
- Bug identification and fixes

## Acceptance Criteria
- Test plan executed completely
- All critical bugs fixed
- Demo stable and reliable
- Test results documented

## Dependencies
Issue #18""",
        "labels": ["testing", "phase-4", "critical", "ai-assisted"],
        "milestone": "Demo Development"
    },
    {
        "title": "Validation with Compliance Professional",
        "body": """**Estimate:** 4 hours + feedback time

## Description
Review demo with AML compliance professional for validation.

## Tasks
- [ ] Identify compliance professional reviewer
- [ ] Prepare demo presentation
- [ ] Conduct review session
- [ ] Gather feedback on:
  - Question structure and wording
  - Risk assessment output format
  - Policy action list usefulness
  - Overall approach
- [ ] Document feedback
- [ ] Prioritize refinements

## Acceptance Criteria
- Review session completed
- Feedback documented
- Professional validates approach
- Refinement priorities identified

## Dependencies
Issues #18, #19""",
        "labels": ["validation", "phase-4", "critical"],
        "milestone": "Validation & Refinement"
    }
]


def create_issues(username, repo_name, token):
    """Create all issues in the GitHub repository."""
    
    g = Github(token)
    
    try:
        repo = g.get_repo(f"{username}/{repo_name}")
        print(f"✅ Connected to repository: {username}/{repo_name}\n")
        
        milestones = {m.title: m for m in repo.get_milestones(state="open")}
        print(f"📊 Found {len(milestones)} milestones")
        
        existing_labels = {l.name for l in repo.get_labels()}
        print(f"🏷️  Found {len(existing_labels)} labels\n")
        
        created_count = 0
        for i, issue_data in enumerate(ISSUES, 1):
            try:
                milestone = None
                if issue_data["milestone"] in milestones:
                    milestone = milestones[issue_data["milestone"]]
                
                labels = [l for l in issue_data["labels"] if l in existing_labels]
                
                issue = repo.create_issue(
                    title=issue_data["title"],
                    body=issue_data["body"],
                    labels=labels,
                    milestone=milestone
                )
                
                created_count += 1
                print(f"✅ Issue #{i}: {issue_data['title']}")
                
            except Exception as e:
                print(f"❌ Error creating issue #{i}: {str(e)}")
        
        print(f"\n🎉 Successfully created {created_count}/{len(ISSUES)} issues!")
        print(f"🔗 View issues at: https://github.com/{username}/{repo_name}/issues")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 create_issues.py USERNAME REPO_NAME")
        sys.exit(1)
    
    username = sys.argv[1]
    repo_name = sys.argv[2]
    
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("❌ Error: GITHUB_TOKEN environment variable not set")
        print("\nSet it with: export GITHUB_TOKEN='your_token_here'")
        sys.exit(1)
    
    print("🚀 GitHub Issue Creator for AML Risk Assessment Tool")
    print("=" * 60)
    print(f"Repository: {username}/{repo_name}")
    print(f"Issues to create: {len(ISSUES)}")
    print("=" * 60)
    print()
    
    response = input("Proceed with issue creation? (yes/no): ")
    if response.lower() not in ["yes", "y"]:
        print("❌ Cancelled")
        sys.exit(0)
    
    print()
    create_issues(username, repo_name, token)


if __name__ == "__main__":
    main()
