# AML Risk Assessment Tool for UK Gambling Industry

[![Project Status](https://img.shields.io/badge/status-planning-yellow)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

An interactive digital tool that guides UK gambling operators through the Money Laundering and Terrorist Financing Risk Assessment process, based on the Gambling Commission's 2023 guidance.

## 🎯 Project Overview

This tool streamlines AML/CTF compliance by presenting sector-specific risks and capturing structured responses about risk applicability and mitigation measures. It generates both a comprehensive risk assessment report and an actionable AML policy development checklist.

## 🚀 Project Status

**Current Phase:** Planning & Content Preparation  
**Target:** Demo/Prototype with simplest Low-risk sector  
**Estimated Timeline:** 2-3 weeks to working demo (AI-assisted development)

## 💡 Problem Statement

Gambling operators must conduct comprehensive AML/CTF risk assessments under UK regulations, but the process is:
- Complex and time-consuming
- Prone to inconsistent documentation
- Difficult to demonstrate compliance to regulators

This tool provides a structured, repeatable process with professional outputs.

## 👥 Target Users

- Compliance officers and MLROs at UK gambling operators
- Senior management responsible for AML compliance oversight
- Covers all 11 UK gambling sector licensing categories

## ⚙️ Core Functionality

### Risk Assessment Workflow

For each identified risk, users answer:

**"Does this risk affect your operations?"**

**Response Options:**
1. **Yes, it does and doesn't need mitigation** → End assessment for this risk
2. **Yes, and mitigation is in place** → Select: Internal/External → Enter brief description
3. **No, it doesn't because of existing mitigation** → Select: Internal/External → Enter brief description
4. **No, it doesn't and we ensure this through controls** → Enter description of controls/checks

## 🤖 AI-Assisted Development

This project leverages AI tools (Claude, ChatGPT, etc.) to accelerate development:

- **Content Extraction**: AI parses PDFs and structures risk data
- **Code Generation**: AI generates React components, logic, and styling
- **Documentation**: AI creates help text, examples, and technical docs
- **Testing**: AI generates comprehensive test cases and scenarios
- **Design**: AI produces mockups, wireframes, and templates

**Estimated Time Savings: ~55%** compared to manual development

## 📊 Sector Coverage

| Sector | Risk Rating |
|--------|-------------|
| Casino, betting and bingo (remote) | High |
| Casino (non-remote) | High |
| Betting (non-remote, off-course) | High |
| Betting (non-remote, on-course) | Medium |
| Bingo (non-remote) | Medium |
| Adult Gaming Centres (AGCs) | Medium |
| Family Entertainment Centres (FECs) | Low |
| Society lotteries and external lottery managers | Low |
| The National Lottery | Low |
| Gambling software | Low |
| Gaming machine technical licences | Low |

## 📋 MVP Features

- [ ] Sector selection (11 categories with risk ratings)
- [ ] Risk library from 2023 Gambling Commission guidance (AI-extracted)
- [ ] Structured questionnaire with conditional logic (AI-generated)
- [ ] Free-text fields for descriptions
- [ ] Progress tracking
- [ ] Export to PDF (AI-implemented)
- [ ] Save and resume capability

## 📤 Output Deliverables

### 1. Risk Assessment Report
- Sector and risk rating context
- Each risk with applicability determination
- Mitigation measures (internal/external)
- Control descriptions
- Date and version control

### 2. AML Policy Action List
- Risks requiring internal mitigation → policy procedures needed
- Controls mentioned → policy documentation required
- Gaps identified → policy development priorities
- External mitigations → policy references
- Areas needing formalization

## 📚 Data Source

Content based on: [Gambling Commission 2023 ML/TF Risk Assessment](https://www.gamblingcommission.gov.uk/print/the-2023-money-laundering-and-terrorist-financing-risks-within-the-british)

## 🗺️ Roadmap

### Phase 1: Content Preparation (Week 1)
- Extract and cate## 🗺️ Roadmap

### Phase 1: Content Preparation (Week 1)
- Extract and categorize risks from GC 2023 guidance
- Identify simplest Low-risk sector for demo
- Create risk library structure
- **Time: 9-11 hours** (with AI assistance)

### Phase 2: Question Design & Sample Build (Week 1-2)
- Refine core functionality questions
- Build prototype with selected sector
- Create sample outputs
- **Time: 16-20 hours** (with AI assistance)

### Phase 3: Output Templates (Week 2)
- Design risk assessment report format
- Design AML policy action list format
- Implement auto-generation logic
- **Time: 14-16 hours** (with AI assistance)

### Phase 4: Demo Development (Week 2-3)
- Technical implementation
- UI/UX design
- End-to-end testing
- Validation with compliance professional
- **Time: 20-22 hours** (with AI assistance)

**Total: 59-69 hours with AI assistance** (vs 131-157 hours manual)  
**Time Savings: ~55%**

## 📂 Project Structure
/AML-Risk-Assessment-Tool
├── README.md
├── .gitignore
├── /docs
│   ├── user-flow.md
│   ├── data-structure.md
│   ├── question-design.md
│   └── output-templates.md
├── /sample-build
│   ├── risk-library-sample.csv
│   └── sample-outputs/
├── /src (when development starts)
└── /tests

## 🤝 Contributing

Contributors are encouraged to use AI tools (Claude, ChatGPT, GitHub Copilot, etc.) to accelerate development while maintaining code quality and ensuring human review of all AI-generated content.

## 🔗 Related Resources

- [Gambling Commission Official Site](https://www.gamblingcommission.gov.uk/)
- [UK Money Laundering Regulations 2017](https://www.legislation.gov.uk/uksi/2017/692/contents)

---

**Next Steps:** See [Issues](../../issues) for current tasks and progress tracking.
