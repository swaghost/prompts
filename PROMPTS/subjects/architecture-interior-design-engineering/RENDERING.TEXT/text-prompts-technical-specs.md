# Technical Specifications - Architectural Text Prompts

## Overview

AI text prompts for generating comprehensive technical specifications following professional standards (AIA, CSI MasterFormat, ABNT, local codes). Use ChatGPT or other AI text tools to quickly create construction specifications, system details, material requirements, and compliance documentation.

**Part of:** [Architectural Professional Text Tools Collection](architectural-professional-text.md)

---

## Use Cases

- **Construction Documents** - Detailed specification sections
- **Permit Applications** - Code compliance documentation
- **Contractor Bid Packages** - Clear material and quality requirements
- **Quality Control Standards** - Acceptance criteria and testing
- **Compliance Documentation** - Meeting code and standard requirements
- **Material Selection** - Detailed product specifications
- **Installation Standards** - Proper execution requirements
- **Warranty Documentation** - Guarantee and maintenance requirements

---

## Basic Prompt Templates

### Complete Project Specification

**Prompt:**

```
Create a technical architectural specification for a 180 m² single-family residence with 3 suites, contemporary style, and a concrete structure, located in São Paulo, Brazil. Follow all applicable ABNT standards.

Include:
- General project information
- Site and foundation specifications
- Structural system specifications
- Architectural finishes by room
- Window and door schedule
- Electrical system requirements
- Plumbing and mechanical systems
- Exterior finishes and landscaping
- Applicable ABNT standard references
- Quality control requirements
```

**When to Use:**

- Complete project specification needed
- Permit submittal preparation
- Comprehensive construction documents
- Full bid package creation
- Owner's project requirements

**Customization:**

- Replace size and program with your project
- Specify architectural style
- Name structural system
- Change location and applicable codes
- Add special features needed

---

### Quick Specification Template

**Prompt:**

```
Generate basic architectural specifications for a [size] [building type] in [location].

Include:
- Foundation type and requirements
- Structural system
- Exterior wall assembly
- Roofing system
- Window and door types
- Interior finishes (by room type)
- Mechanical/electrical/plumbing systems
- Applicable building codes
```

**When to Use:**

- Early document development
- Preliminary specifications
- Contractor discussions
- Budget specification basis
- Design development phase

---

## System-Specific Specifications

### Exterior Cladding System

**Prompt:**

```
Generate detailed specifications for [cladding system: brick/stone/metal panel/curtain wall/EIFS/fiber cement/wood siding] exterior cladding for [project type].

Include:
- Material specifications (type, grade, finish, color)
- Performance requirements (weather resistance, thermal, durability)
- Installation methods and sequence
- Substrate and backing requirements
- Flashing and waterproofing details
- Joint and sealant specifications
- Quality standards and testing protocols
- Applicable codes and standards (ASTM, local)
- Warranty requirements
- Submittal requirements (samples, shop drawings, product data)
- Contractor qualifications
- Maintenance requirements
```

**Example:**

```
Generate detailed specifications for standing seam metal roof system for commercial office building in coastal environment.

Include:
- Material specifications (metal type, gauge, finish, color)
- Performance requirements (wind uplift, weather resistance, thermal, corrosion resistance)
- Installation methods and sequence
- Substrate and backing requirements
- Flashing and waterproofing details
- Joint and panel connection specifications
- Quality standards and testing protocols
- Applicable codes and standards (ASTM, UL, FM, local)
- Warranty requirements (25-year weathertightness)
- Submittal requirements (samples, shop drawings, product data)
- Contractor qualifications (certified installer)
- Maintenance requirements
```

**When to Use:**

- Specific system design
- Bid alternates needed
- Detail level specification
- Complex assemblies
- Performance-critical systems

---

### Roofing System Specification

**Prompt:**

```
Create comprehensive roofing specification for [roof type: flat/low-slope/steep slope] roof using [system: TPO/EPDM/modified bitumen/metal/tile/shingle] for [building type].

Detail:
- Roof assembly (deck, insulation, membrane/covering)
- Material properties and standards
- Slope and drainage requirements
- Flashing and edge details
- Penetration and equipment curb requirements
- Installation procedures
- Quality assurance and testing
- Warranty (material and installation)
- Maintenance program
- Applicable standards (NRCA, manufacturer, ASTM)
```

**When to Use:**

- Critical waterproofing
- Complex roof configurations
- High-performance requirements
- Warranty-specific projects
- Specialized systems

---

### Foundation System Specification

**Prompt:**

```
Specify foundation system for [project] on [soil conditions] supporting [structural system].

Include:
- Foundation type (spread footings/mat/piles/caissons)
- Concrete specifications (strength, mix design, admixtures)
- Reinforcement requirements (size, spacing, cover)
- Excavation and formwork requirements
- Waterproofing and drainage systems
- Under-slab requirements (vapor barrier, insulation, fill)
- Quality control (testing, inspection points)
- Cold weather/hot weather provisions
- Applicable standards (ACI, ASTM, local)
```

---

### Window and Glazing Specification

**Prompt:**

```
Develop window and glazing specifications for [building type] in [climate zone].

Specify:
- Window type and operating mode
- Frame material and finish
- Glazing specifications (U-value, SHGC, VLT, thickness)
- Performance requirements (air infiltration, water penetration, structural)
- Hardware and accessories
- Installation and flashing requirements
- Testing and certification (NFRC, AAMA)
- Energy code compliance
- Warranty requirements
- Color and finish options
```

**Example:**

```
Develop window and glazing specifications for commercial office building in hot-humid climate (Miami).

Specify:
- Aluminum curtain wall system with operable windows
- Thermally broken aluminum frames, dark bronze anodized finish
- Low-E insulated glazing (U-value ≤0.30, SHGC ≤0.25, VLT ≥40%)
- Performance requirements (air infiltration <0.06 cfm/ft², water penetration 12 psf, wind load per ASCE 7)
- Hurricane impact resistant glazing per Florida Building Code
- Stainless steel hardware, corrosion resistant
- Installation per AAMA specifications with silicone sealants
- Testing per NFRC, AAMA certification required
- Florida Energy Code compliance
- 10-year warranty on glass, 20-year on frame finish
```

---

### Interior Finishes Specification

**Prompt:**

```
Specify interior finishes for [space type: office/residential/retail/healthcare/education] including:

Flooring:
- Material type and specification
- Installation requirements
- Transition details

Walls:
- Surface preparation
- Paint or wallcovering specifications
- Special finishes

Ceilings:
- System type
- Finish requirements
- Access and integration

Millwork:
- Material and construction
- Finish specifications
- Hardware

Include:
- Performance requirements
- Accessibility compliance
- Maintenance considerations
- Warranty requirements
```

---

### Mechanical System Specification

**Prompt:**

```
Generate HVAC system specifications for [building type, size] in [climate zone]:

System Type: [forced air/radiant/VRF/chilled water/etc.]

Include:
- Equipment specifications (capacity, efficiency, manufacturer standards)
- Distribution system (ductwork/piping materials, insulation)
- Controls and automation
- Ventilation and air quality requirements
- Energy efficiency requirements (ASHRAE 90.1 or local code)
- Installation standards
- Testing, adjusting, and balancing (TAB)
- Commissioning requirements
- Warranty and maintenance
- Applicable standards (ASHRAE, SMACNA, manufacturer)
```

---

### Electrical System Specification

**Prompt:**

```
Create electrical specifications for [building type]:

Cover:
- Service and distribution (voltage, capacity, panel locations)
- Branch circuitry and receptacle requirements
- Lighting systems (fixture types, controls)
- Emergency and exit lighting
- Fire alarm system integration
- Data and communication systems
- Special systems (security, AV, etc.)
- Energy code compliance
- Installation standards (NEC, local amendments)
- Testing and commissioning
- Labeling and documentation
```

---

## Specialty Specifications

### Sustainable/Green Building

**Prompt:**

```
Create green building specifications for [project description] targeting [LEED/BREEAM/Green Globes/Net Zero/Passive House] certification at [certification level].

Address:
- Sustainable site development (stormwater, heat island, light pollution)
- Energy efficiency requirements (envelope, systems, renewables)
- Water conservation systems (fixtures, irrigation, rainwater harvesting)
- Materials and resources (recycled content, regional materials, FSC wood, low-VOC)
- Indoor environmental quality (air quality, daylighting, thermal comfort, acoustics)
- Innovation opportunities
- Measurement and verification
- Documentation and commissioning requirements
- Referenced standards (ASHRAE 90.1, ASTM, GreenGuard, etc.)
```

**Example:**

```
Create green building specifications for 5,000 m² office building targeting LEED Gold certification.

Address:
- Sustainable site development (bioretention for stormwater, vegetated roof to reduce heat island, dark-sky compliant exterior lighting)
- Energy efficiency requirements (R-30 roof, R-20 walls, triple-glazed windows U-0.22, high-efficiency VRF system, LED lighting with daylight/occupancy controls, 50kW rooftop solar PV)
- Water conservation systems (low-flow fixtures 30% below baseline, native/adaptive landscaping, drip irrigation with soil moisture sensors)
- Materials and resources (20% recycled content, 20% regional materials within 500 miles, FSC-certified wood, low-VOC paints/adhesives/sealants/carpets)
- Indoor environmental quality (CO2 monitoring and ventilation control, 75% spaces with daylighting, operable windows, acoustic design per WELL standards)
- Enhanced commissioning with M&V plan
- Referenced standards (ASHRAE 90.1-2016, ASTM, GreenGuard Gold, FSC)
```

---

### Historic Preservation

**Prompt:**

```
Develop technical specifications for sensitive renovation of [historic building description] built in [year], designated [landmark status if applicable].

Cover:
- Historic preservation standards compliance (Secretary of Interior Standards, local requirements)
- Existing conditions assessment and documentation requirements
- Intervention philosophy and approach (preserve, restore, rehabilitate, reconstruct)
- Material matching specifications (masonry, wood, metal, glass)
  - Analysis and testing requirements
  - Sourcing compatible materials
  - Matching techniques and finishes
- Modern code compliance strategies (life safety, accessibility, energy)
  - Minimal impact approaches
  - Reversible interventions where possible
- Building system integration (HVAC, electrical, plumbing)
  - Concealed routing
  - Minimal historic fabric removal
- Craftsmanship and trade qualification requirements
  - Specialized skills needed
  - Mock-up and approval process
- Documentation requirements (photographic, measured drawings, material samples)
- Review and approval process (preservation officer, review board)
```

---

### Accessibility/Universal Design

**Prompt:**

```
Generate accessibility specifications for [project] ensuring compliance with [ADA/local accessibility code/universal design principles].

Include:
- Accessible routes and entrances
- Door and corridor widths
- Ramp and lift requirements
- Accessible toilet rooms (layout, clearances, fixtures, grab bars)
- Kitchen accessibility (if applicable)
- Signage (tactile, visual contrast, Braille)
- Finish selections (slip resistance, visual contrast, tactile)
- Hardware specifications (lever handles, automatic operators)
- Elevator requirements
- Communication systems (visual and audible alarms)
- Assistive listening systems
- Testing and verification procedures
```

---

### Fire-Rated Assemblies

**Prompt:**

```
Specify fire-rated construction assemblies for [building type/occupancy]:

Include:
- Fire-rated wall assemblies (1-hour, 2-hour, etc.)
  - Material specifications
  - Construction details
  - UL/FM tested assemblies
- Fire-rated floor/ceiling assemblies
- Fire doors and frames (rating, hardware, installation)
- Firestopping and through-penetrations
- Fire dampers in duct penetrations
- Smoke partitions and barriers
- Exit stair and corridor construction
- Fire-resistive coatings or treatments
- Inspection and testing requirements
- Applicable standards (NFPA, UL, IBC)
```

---

### Acoustical Specifications

**Prompt:**

```
Develop acoustical specifications for [space type: classroom/theater/recording studio/multi-family/office/etc.] achieving [performance criteria: STC/IIC ratings, reverberation time, background noise level].

Specify:
- Sound isolation assemblies (walls, floors/ceilings)
  - STC and IIC ratings required
  - Construction details
- Acoustical treatments (absorption, diffusion)
- Noise control for mechanical systems (NC/RC curves)
- Impact isolation systems
- Door and window acoustical performance
- Resilient channels and isolation clips
- Acoustical sealants and gaskets
- Field testing requirements
- Commissioning and verification
- Applicable standards (ASTM E90, E492, AHRI, etc.)
```

---

## Format-Specific Requests

### CSI MasterFormat Organization

**Add to any specification prompt:**

```
Organize specification by CSI MasterFormat divisions:

Division 01: General Requirements
Division 02: Existing Conditions
Division 03: Concrete
Division 04: Masonry
Division 05: Metals
Division 06: Wood, Plastics, Composites
Division 07: Thermal and Moisture Protection
Division 08: Openings
Division 09: Finishes
[continue with applicable divisions]

Use standard section format with:
- Section number and title
- Three-part format (Part 1 General, Part 2 Products, Part 3 Execution)
```

---

### Three-Part Specification Format

**Add to any prompt:**

```
Format each specification section in three parts:

PART 1 - GENERAL
1.1 Summary
1.2 Related Sections
1.3 References
1.4 Submittals
1.5 Quality Assurance
1.6 Delivery, Storage, and Handling
1.7 Project Conditions
1.8 Warranty

PART 2 - PRODUCTS
2.1 Materials
2.2 Equipment
2.3 Accessories
2.4 Mixes/Fabrication

PART 3 - EXECUTION
3.1 Examination
3.2 Preparation
3.3 Installation
3.4 Field Quality Control
3.5 Adjusting
3.6 Cleaning
3.7 Protection
```

---

### Performance Specification

**Add to any prompt:**

```
Write as performance specification rather than prescriptive:
- State required performance criteria and end results
- Allow contractor/manufacturer flexibility in means and methods
- Specify testing and acceptance criteria
- Do not specify specific products (unless required)
- Focus on what must be achieved, not how
```

---

### Proprietary Specification

**Add to any prompt:**

```
Write as proprietary specification:
- Name specific manufacturers and products
- Include model numbers and part numbers
- State "no substitutions" or "approved equal" as appropriate
- Provide complete product data requirements
- Ensure specified products are available
```

---

## Enhancement Techniques

### Add Submittal Requirements

**Add to prompt:**

```
Include detailed submittal requirements:
- Product data sheets
- Shop drawings
- Samples (size and quantity)
- Certificates (fire rating, testing, compliance)
- Manufacturer's instructions
- Warranty documents
- Test reports
- Closeout documentation
- Operations and maintenance manuals
```

---

### Include Testing & QC

**Add to prompt:**

```
Specify quality control measures:
- Field testing requirements (when, what, frequency)
- Laboratory testing (samples, standards)
- Mock-ups and samples (location, size, approval process)
- Inspection hold points
- Acceptance criteria
- Non-conformance procedures
- Documentation of testing
- Third-party testing/certification if required
```

---

### Specify Qualifications

**Add to prompt:**

```
Include contractor and installer qualifications:
- Years of experience required
- Similar project examples
- Manufacturer certifications or training
- License requirements
- Insurance requirements
- Safety certifications
- Quality management systems
- References
```

---

### Define Warranty Requirements

**Add to prompt:**

```
Specify warranty requirements:
- Duration (material and workmanship separate if applicable)
- Coverage (what is included/excluded)
- Transferability
- Maintenance requirements to maintain validity
- Exclusions and limitations
- Warranty documentation and registration
- Extended warranty options
- Service response time
```

---

## Specification by Building Type

### Residential Specification

**Prompt:**

```
Create residential construction specifications for [single-family/multi-family/custom home] project:
- Foundation and structure appropriate to [site conditions]
- Exterior envelope (siding, roofing, windows, doors)
- Insulation and air sealing (meet energy code)
- Interior finishes (flooring, walls, ceilings, trim)
- Kitchen and bathroom specifications
- Mechanical systems (HVAC, plumbing, electrical)
- Built-in features (cabinets, counters, closets)
- Exterior features (decks, patios, landscaping)
- Quality level: [economy/standard/custom/luxury]
- Applicable codes (IRC, local amendments)
```

---

### Commercial Office Specification

**Prompt:**

```
Generate commercial office building specifications:
- Building shell (structure, envelope, roofing)
- Core and shell MEP systems
- Elevator and life safety systems
- Base building finishes
- Tenant improvement specifications (if applicable)
- Accessibility compliance (ADA)
- Energy efficiency (ASHRAE 90.1, Title 24, etc.)
- Parking and site work
- Fire protection and life safety
- Building codes (IBC, NFPA, local)
- Sustainability goals (if applicable)
```

---

### Retail Specification

**Prompt:**

```
Specify retail construction for [retail type: restaurant/store/shopping center]:
- Storefront and entrance systems
- Display window specifications
- Interior finishes (durable, maintainable)
- Lighting systems (display, general, accent)
- HVAC for high occupancy
- Kitchen/service areas (if restaurant)
- Security systems
- Signage allowances and requirements
- Accessibility requirements
- High-traffic material specifications
- Building codes (IBC, health department if food service)
```

---

### Healthcare Specification

**Prompt:**

```
Create healthcare facility specifications for [clinic/hospital/medical office]:
- Infection control surfaces and finishes
- Hand hygiene stations
- Medical gas systems (if applicable)
- Specialized HVAC (filtration, pressure relationships)
- Clinical equipment provisions
- Accessible patient rooms and toilet rooms
- Privacy and HIPAA considerations
- Durable, cleanable finishes
- Nurse call and communication systems
- Emergency power systems
- Applicable codes (FGI Guidelines, NFPA 99, state health department)
```

---

## Code and Standard References

### Specify Applicable Codes

**Add to any prompt:**

```
Reference all applicable codes and standards:
- Building code (IBC, IRC, NBC, or local)
- Energy code (IECC, ASHRAE 90.1, Title 24, local)
- Plumbing code (IPC, UPC, local)
- Mechanical code (IMC, UMC, local)
- Electrical code (NEC, local amendments)
- Fire code (IFC, NFPA, local)
- Accessibility (ADA, ICC A117.1, local)
- Structural (ASCE 7, ACI, AISC, AWC)
- Material standards (ASTM, ANSI, etc.)
- Green building (LEED, IECC, local)
```

---

### International/Regional Codes

**For non-US projects, specify:**

```
For project in [country], reference applicable local standards:
- [National building code]
- [Energy/sustainability requirements]
- [Local/regional amendments]
- Material standards (ISO, national standards body)
- Professional practice requirements
- Language requirements for documentation
```

**Example:**

```
For project in São Paulo, Brazil, reference:
- ABNT NBR standards (specifically list applicable)
- São Paulo municipal building code
- Brazilian accessibility standards (NBR 9050)
- Energy efficiency (PROCEL, RTQ)
- Environmental requirements (CONAMA)
- Professional requirements (CAU, CREA)
```

---

## Specification Coordination

### Multi-Discipline Coordination

**Prompt:**

```
Ensure specification coordination between architectural, structural, mechanical, electrical, and plumbing disciplines for [project]:

Identify:
- Interface requirements between disciplines
- Shared system specifications (fire protection, building automation)
- Coordination items (penetrations, clearances, access)
- Responsibility matrix for each specification section
- Cross-references between specification sections
- Drawing-to-spec coordination requirements
- Conflicting requirements to resolve
```

---

### Drawing-Specification Coordination

**Add to prompt:**

```
Ensure coordination between drawings and specifications:
- Note on drawings: "Refer to specifications for detailed requirements"
- Reference specification sections on drawings
- Avoid duplicating information (specs take precedence)
- Coordinate schedules (door, window, finish, equipment)
- Ensure details match specified assemblies
- Material legends consistent with specs
```

---

## Quality Assurance Sections

### Inspection and Testing Plan

**Prompt:**

```
Create inspection and testing plan for [project type] specifying:

For each major system:
- Inspection hold points (before covering work)
- Testing required (type, frequency, standard)
- Mock-up requirements (location, size, approval process)
- Quality control sampling rates
- Acceptance criteria
- Non-conformance procedures
- Responsible parties (contractor, third-party, architect)
- Documentation requirements
- Corrective action process
```

---

### Shop Drawing Requirements

**Prompt:**

```
Specify shop drawing and submittal requirements for [project]:

For each major element:
- Required shop drawings and level of detail
- Product data requirements
- Sample requirements (size, quantity, finishes)
- Number of copies required
- Submission timing (lead time before installation)
- Review and approval process
- Resubmittal requirements if rejected
- Incorporation of comments
- Electronic format requirements
```

---

## Follow-Up Refinement Prompts

### Adding Detail

After initial specification:

```
"Expand section [number/name] to include more detail on [specific aspect: installation procedures/material properties/testing requirements]."
```

---

### Alternative Products

```
"For the specified [system/material], provide three approved-equal alternatives with equivalent performance characteristics and pricing."
```

---

### Sustainability Enhancement

```
"Revise this specification to incorporate [specific green building requirements: higher recycled content/lower VOC/regional materials/enhanced energy performance]."
```

---

### Cost Reduction

```
"Suggest cost-effective alternatives for the specified [system/materials] that maintain acceptable performance and quality."
```

---

### Compliance Verification

```
"Review this specification against [specific code or standard] and identify any non-compliance or missing requirements."
```

---

## Output Format Examples

### Standard Three-Part Spec Format

```
SECTION 09 51 00
ACOUSTICAL CEILINGS

PART 1 - GENERAL

1.1 SUMMARY
    A. Section includes:
       1. Acoustical ceiling panels
       2. Exposed suspension system
       3. Hold-down clips and accessories

1.2 REFERENCES
    A. ASTM C367 - Strength Properties of Prefabricated Architectural Acoustical Panels
    B. ASTM E1264 - Classification of Acoustical Ceiling Products

1.3 SUBMITTALS
    A. Product Data: Manufacturer's data sheets
    B. Shop Drawings: Reflected ceiling plans showing layout
    C. Samples: 300mm x 300mm samples of each panel type and finish

1.4 QUALITY ASSURANCE
    A. Installer Qualifications: Minimum 5 years experience with similar work

PART 2 - PRODUCTS

2.1 MANUFACTURERS
    A. Armstrong World Industries
    B. USG Corporation
    C. Or approved equal

2.2 ACOUSTICAL PANELS
    A. Type: Mineral fiber panels
    B. Size: 600mm x 1200mm x 19mm thickness
    C. Edge Detail: Square edge, reveal edge
    D. Finish: Factory-painted white, matte finish
    E. Performance:
       1. NRC: Minimum 0.70
       2. CAC: Minimum 35
       3. Light Reflectance: Minimum 0.83

PART 3 - EXECUTION

3.1 EXAMINATION
    A. Verify that overhead work is complete
    B. Verify that HVAC system is operational

3.2 INSTALLATION
    A. Install per manufacturer's instructions
    B. Coordinate with lighting and HVAC
    C. Maintain 19mm clearance to walls

3.3 CLEANING
    A. Clean panels and grid after installation

END OF SECTION
```

---

## Professional Use Guidelines

### Appropriate Applications

✅ **Good for:**

- Initial specification drafts
- Standard specification sections
- Template generation
- Educational specifications
- Early design phase specs
- Bid package starting points

✅ **With Professional Review:**

- Final construction documents (must be reviewed and edited)
- Permit submittals (verify code compliance)
- Contract documents (legal review)
- Complex technical specifications (verify technical accuracy)

---

### Limitations & Requirements

❗ **Important:**

- AI specifications are starting points requiring professional review
- Code references may not be current or complete
- Local amendments and requirements may not be included
- Technical details must be verified by licensed professionals
- Product availability and specifications change
- Legal implications of specification language
- Professional liability for specification errors

❗ **Always:**

- Review and edit AI output thoroughly
- Verify code and standard references are current
- Check product availability and specifications
- Ensure specification coordination
- Have specifications reviewed by licensed professionals
- Update specifications to match project conditions
- Verify consistency between drawings and specs
- Maintain professional liability insurance

---

### Risk Management

1. **Professional Seal Required** - Specifications must be reviewed and sealed by licensed professionals
2. **Verify Technical Accuracy** - Check all technical data and requirements
3. **Update Code References** - Ensure codes and standards are current
4. **Coordination Check** - Verify consistency across all disciplines
5. **Legal Review** - Contract language should be reviewed by attorney
6. **Product Verification** - Confirm specified products exist and are available
7. **Performance Criteria** - Verify performance requirements are achievable
8. **Testing Standards** - Ensure testing references are current and applicable

---

## Related Prompt Types

- [Cost Estimation](text-prompts-cost-estimation.md) - For budget and feasibility
- [Project Briefs](text-prompts-project-briefs.md) - Requirements documentation
- [Design Concepts](text-prompts-design-concepts.md) - Concept generation
- [Checklists](text-prompts-checklists.md) - QC and compliance verification

---

**See Also:** [Main Text Prompts Guide](architectural-professional-text.md) for all prompt types and general best practices.
