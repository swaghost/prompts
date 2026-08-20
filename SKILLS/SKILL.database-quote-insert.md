---
name: database-quote-insert
description: "Insert quotes into database using stored procedure with duplicate checking and IMAGE EXTRACTION. Supports: 1) AUTOMATIC mode - paste quote image, AI extracts quote/author/context/meaning/tags and inserts. 2) MANUAL mode - provide text details. Use for: adding quotes from images, saving quote data, OCR quote extraction, inserting quotes with AI-generated context and tags, calling CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING."
argument-hint: "Extract and save this quote"
user-invocable: true
---

# Database Quote Insert Skill

## Purpose

This skill enables you to insert quotes into a database using the `CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING` stored procedure. 

**Two Input Modes:**
1. **🖼️ IMAGE MODE (Recommended)**: Paste a quote image → AI extracts quote, author, context, meaning, and generates tags → inserts to database
2. **✍️ MANUAL MODE**: Provide quote details manually → inserts to database

The skill handles duplicate checking, captures output parameters (return value, message, quote ID), and provides complete feedback on the operation.

## When to Use

Use this skill when:

- **User pastes a quote image** and says "extract this quote" or "add this to database"
- Adding quotes from screenshots, social media images, or photos
- User wants to add a quote to the database (text mode)
- Storing quote data in SQL database with author, context, meaning
- Need AI to research context and generate tags automatically
- Executing database insert operations with stored procedure
- Database operations requiring connection string configuration

## Configuration File Setup (Recommended)

For security, store your database connection details in a git-ignored configuration file:

1. Copy `db-config.example.json` to `db-config.json`
2. Fill in your actual connection string and query
3. The file is automatically git-ignored to keep credentials safe

**Configuration file structure:**

```json
{
  "connectionString": "Server=localhost;Database=Basics2025;User Id=YourUser;Password=YourPass;",
  "storedProcedure": "CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING",
  "databaseType": "sqlserver",
  "defaultUserId": 7
}
```

## Stored Procedure Details

The skill calls `CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING` with the following parameters:

**Input Parameters:**

- `@QuoteContent` (nvarchar(max)) - The quote text
- `@QuoteParaphrased` (bit) - Was it paraphrased? (default: 0 = No)
- `@QuoteAttributionName` (nvarchar(2000)) - The author/source
- `@QuoteAttributionContext` (nvarchar(2000)) - Context in which it was written
- `@QuoteMeaning` (nvarchar(max)) - The meaning/interpretation
- `@QuoteMeaningIntentionallyLeftBlank` (bit) - If no meaning provided, set to 1
- `@AddedByUserID` (bigint) - User ID (default: 7 from config)
- `@QuoteTags` (nvarchar(max)) - Tags separated by '|'

**Output Parameters:**

- `@ReturnVal` (INT) - 1 = OK (new quote), 2 = FOUND (duplicate)
- `@ReturnMsg` (NVARCHAR(500)) - Status message
- `@QuoteID` (bigint) - New or existing quote ID

## Quick Start - Installation & Usage

### Installation Steps

1. **Copy configuration template:**
   ```powershell
   Copy-Item db-config.example.json db-config.json
   ```

2. **Edit db-config.json** with your SQL Server credentials:
   ```json
   {
     "connectionString": "Server=YOUR_SERVER;Database=Basics2025;User Id=YOUR_USER;Password=YOUR_PASSWORD;",
     "storedProcedure": "CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING",
     "databaseType": "sqlserver",
     "defaultUserId": 7
   }
   ```

3. **Reload VS Code** to activate the skill:
   - Press `Ctrl+Shift+P`
   - Type "Developer: Reload Window"
   - Or restart VS Code

### Usage - Image Mode (Recommended) 🖼️

1. **Find a quote image** (screenshot, social media post, photo of book page, etc.)
2. **Paste the image** into Copilot chat
3. **Say:** "Extract and save this quote" or "Add this quote to database"
4. **Review** the AI-extracted quote, author, context, meaning, and tags
5. **Confirm** by saying "yes" or provide corrections
6. **Done!** The quote is inserted and you get the QuoteID

### Usage - Manual Mode ✍️

1. **Invoke the skill:**
   - Type: `/database-quote-insert`
   - Or say: "Add this quote to database: [your quote text]"

2. **Provide details** when prompted:
   - Quote text (required)
   - Author (optional)
   - Context (optional)
   - Meaning (optional)
   - Tags (optional, pipe-separated like "motivation|business")

3. **Review results:**
   - ✓ SUCCESS = New quote added with QuoteID
   - ⚠ DUPLICATE = Quote already exists with existing QuoteID

## Required Information

Before executing, the skill needs:

1. **Database Configuration** - Either from `db-config.json` file or provided directly:
   - Connection String (server, database, credentials)
   - Stored Procedure name: `CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING`
   - Default User ID (from config)

2. **Quote Data** - The actual values to insert:
   - **Quote Content** (required) - The quote text
   - **Author/Attribution Name** (optional) - Who said/wrote it
   - **Attribution Context** (optional) - When/where/why it was said
   - **Quote Meaning** (optional) - Your interpretation or explanation
   - **Tags** (optional) - Categories separated by '|' (e.g., "motivation|business|leadership")
   - **Paraphrased?** (optional) - Set to true if you paraphrased the original

## Execution Procedure

### Step 0A: Determine Input Mode

**Check if user provided an image:**

- If user attached/pasted an image → **IMAGE EXTRACTION MODE** (proceed to Step 0B)
- If user provided text only → **MANUAL MODE** (proceed to Step 0C)

### Step 0B: IMAGE EXTRACTION MODE

When user pastes a quote image, automatically perform these steps:

1. **Analyze the image** using vision capabilities:
   - Extract the quote text (main content)
   - Identify author/speaker name
   - Capture any visible source attribution

2. **Research context if needed:**
   - If the quote is recognizable but context is missing from image, search for:
     - Original source (speech, book, interview, article)
     - Historical context (when and where it was said)
     - Author background relevant to the quote
   - If completely unable to find context, indicate "Context not found"

3. **Infer meaning:**
   - Analyze what the quote is conveying
   - Consider the original context
   - Provide 2-3 sentence interpretation
   - If meaning is unclear, leave blank and set flag

4. **Generate tags:**
   - Create 3-8 relevant tags based on:
     - Topic/theme (motivation, business, life, leadership, philosophy)
     - Domain (technology, sports, politics, education, entrepreneurship)
     - Emotional tone (inspirational, cautionary, humorous, reflective)
   - Format as pipe-separated: `motivation|leadership|innovation`

5. **Present extraction results to user for confirmation:**

```
📸 Extracted from image:

Quote: "[extracted quote text]"
Author: [name or "Unknown"]
Context: [source/occasion or "Not specified"]
Meaning: [interpretation or "Not specified"]
Tags: [tag1|tag2|tag3]

Ready to insert? Say "yes" to proceed, or provide corrections.
```

6. **Wait for user confirmation:**
   - If approved: proceed to Step 2 (Validate Inputs)
   - If corrections provided: update the extracted data, then proceed

### Step 0C: Check for Configuration File (MANUAL MODE)

First, check if `db-config.json` exists in the workspace:

- If exists: Read the connection string, table name, and insert query from the file
- If not exists: Proceed to ask the user for these details

### Step 1: Gather Requirements (MANUAL MODE ONLY)

**If configuration file exists:**

- Only ask for the quote data
- Use connection string, stored procedure name, and user ID from `db-config.json`

Use `vscode_askQuestions` to collect quote information:

```
Questions:
1. "Quote Content" (required) - The actual quote text
2. "Author/Attribution" (optional) - Who said or wrote this?
3. "Context" (optional) - When/where/why was this said?
4. "Meaning" (optional) - What does this quote mean to you?
5. "Tags" (optional) - Categories separated by | (e.g. motivation|leadership)
6. "Paraphrased?" (optional) - Did you paraphrase this? (yes/no)
```

**Note:** The skill will automatically set `@QuoteMeaningIntentionallyLeftBlank = 1` if meaning is not provided.

### Step 2: Validate Inputs

Before executing, verify:

- Connection string is properly formatted
- Quote content is provided (required)
- Tags format is correct if provided (separated by '|')
- All optional fields have appropriate defaults

### Step 3: Execute Stored Procedure

Use PowerShell to call the stored procedure with output parameters:

```powershell
# Load configuration
$config = Get-Content "db-config.json" | ConvertFrom-Json
$connectionString = $config.connectionString
$storedProc = $config.storedProcedure
$defaultUserId = $config.defaultUserId

# Quote data from user input
$quoteContent = "[Quote text from user]"
$quoteParaphrased = 0  # 0 = No, 1 = Yes
$attributionName = "[Author from user or NULL]"
$attributionContext = "[Context from user or NULL]"
$quoteMeaning = "[Meaning from user or NULL]"
$meaningLeftBlank = if ([string]::IsNullOrWhiteSpace($quoteMeaning)) { 1 } else { 0 }
$quoteTags = "[Tags from user or NULL]"  # e.g., "motivation|leadership|business"
$addedByUserId = $defaultUserId

# Create connection and command
$connection = New-Object System.Data.SqlClient.SqlConnection($connectionString)
$command = $connection.CreateCommand()
$command.CommandType = [System.Data.CommandType]::StoredProcedure
$command.CommandText = $storedProc

# Add input parameters
$command.Parameters.AddWithValue("@QuoteContent", $quoteContent) | Out-Null
$command.Parameters.AddWithValue("@QuoteParaphrased", $quoteParaphrased) | Out-Null
$command.Parameters.AddWithValue("@QuoteAttributionName", $(if ($attributionName) { $attributionName } else { [DBNull]::Value })) | Out-Null
$command.Parameters.AddWithValue("@QuoteAttributionContext", $(if ($attributionContext) { $attributionContext } else { [DBNull]::Value })) | Out-Null
$command.Parameters.AddWithValue("@QuoteMeaning", $(if ($quoteMeaning) { $quoteMeaning } else { [DBNull]::Value })) | Out-Null
$command.Parameters.AddWithValue("@QuoteMeaningIntentionallyLeftBlank", $meaningLeftBlank) | Out-Null
$command.Parameters.AddWithValue("@AddedByUserID", $addedByUserId) | Out-Null
$command.Parameters.AddWithValue("@QuoteTags", $(if ($quoteTags) { $quoteTags } else { [DBNull]::Value })) | Out-Null

# Add output parameters
$returnVal = $command.Parameters.Add("@ReturnVal", [System.Data.SqlDbType]::Int)
$returnVal.Direction = [System.Data.ParameterDirection]::Output

$returnMsg = $command.Parameters.Add("@ReturnMsg", [System.Data.SqlDbType]::NVarChar, 500)
$returnMsg.Direction = [System.Data.ParameterDirection]::Output

$quoteId = $command.Parameters.Add("@QuoteID", [System.Data.SqlDbType]::BigInt)
$quoteId.Direction = [System.Data.ParameterDirection]::Output

try {
    $connection.Open()
    $command.ExecuteNonQuery() | Out-Null

    # Read output parameters
    $retVal = $returnVal.Value
    $retMsg = $returnMsg.Value
    $newQuoteId = $quoteId.Value

    # Report results
    if ($retVal -eq 1) {
        Write-Host "✓ SUCCESS: Quote added successfully!" -ForegroundColor Green
        Write-Host "  Quote ID: $newQuoteId"
        Write-Host "  Message: $retMsg"
    } elseif ($retVal -eq 2) {
        Write-Host "⚠ DUPLICATE: This quote already exists" -ForegroundColor Yellow
        Write-Host "  Existing Quote ID: $newQuoteId"
        Write-Host "  Message: $retMsg"
    } else {
        Write-Host "⚠ UNKNOWN: Unexpected return value: $retVal" -ForegroundColor Yellow
        Write-Host "  Message: $retMsg"
    }

} catch {
    Write-Host "✗ ERROR: Database operation failed" -ForegroundColor Red
    Write-Host "  $_" -ForegroundColor Red
} finally {
    $connection.Close()
}
```

### Step 4: Interpret and Report Results

After execution, interpret the output parameters:

**Return Value Meanings:**

- `@ReturnVal = 1` → SUCCESS: New quote created
- `@ReturnVal = 2` → DUPLICATE: Quote already exists in database

**Report to user:**

1. Success status (new or duplicate)
2. Quote ID (new or existing)
3. Return message from stored procedure
4. Any errors encountered

## Error Handling

Common errors and solutions for stored procedure execution:

| Error                           | Likely Cause                     | Solution                                                                    |
| ------------------------------- | -------------------------------- | --------------------------------------------------------------------------- |
| Connection timeout              | Wrong server address or firewall | Verify server address and network connectivity                              |
| Login failed                    | Wrong credentials                | Check username/password in connection string                                |
| Could not find stored procedure | Wrong procedure name or schema   | Verify procedure exists: `CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING` |
| Parameter mismatch              | Missing or wrong parameter names | Check stored procedure signature matches code                               |
| Null value error                | Required parameter is null       | Ensure QuoteContent is provided                                             |
| Foreign key constraint          | Invalid @AddedByUserID           | Verify User ID exists in the Users table                                    |
| Type conversion error           | Wrong data type for parameter    | Verify bit (0/1) for boolean, nvarchar for text                             |

## Security Best Practices

1. **Stored Procedure Benefits** - Using stored procedures provides built-in SQL injection protection
2. **Connection string security** - Store `db-config.json` locally (git-ignored), never commit credentials
3. **Least privilege** - Database account should only have EXECUTE permission on this stored procedure
4. **Audit logging** - Stored procedure tracks @AddedByUserID for accountability
5. **Input validation** - Validate quote text length (nvarchar(max) has limits) before inserting
6. **Duplicate checking** - Built-in duplicate detection prevents data redundancy

## Example Workflows

### Example 1: Image Extraction (RECOMMENDED)

```
User: [Pastes an image containing a quote in elegant typography]

User: "Extract and save this quote"

Agent Actions:
1. Analyzes image using vision capabilities
2. Extracts quote: "The best time to plant a tree was 20 years ago. The second best time is now."
3. Identifies no visible author in image
4. Searches and finds: Chinese proverb
5. Infers context: "Ancient wisdom about procrastination and taking action"
6. Generates meaning: "Don't let past missed opportunities prevent you from acting now. It's never too late to start something worthwhile, even if you wish you'd started earlier."
7. Creates tags: "wisdom|action|procrastination|time-management|chinese-proverb"

8. Presents to user:
   📸 Extracted from image:
   
   Quote: "The best time to plant a tree was 20 years ago. The second best time is now."
   Author: Chinese Proverb
   Context: Ancient wisdom about procrastination and taking action
   Meaning: Don't let past missed opportunities prevent you from acting now. It's never too late to start something worthwhile, even if you wish you'd started earlier.
   Tags: wisdom|action|procrastination|time-management|chinese-proverb
   
   Ready to insert? Say "yes" to proceed.

User: "yes"

Agent Actions:
9. Reads db-config.json for connection details
10. Executes stored procedure with extracted data
11. Reports: "✓ SUCCESS: Quote added successfully! Quote ID: 1236"
```

### Example 2: Simple Quote (Manual Mode)

```
User: "Add this quote: 'The only way to do great work is to love what you do' by Steve Jobs"

Agent Actions:
1. Read db-config.json for connection details
2. Gather quote data:
   - Quote Content: "The only way to do great work is to love what you do"
   - Author: "Steve Jobs"
   - Context: (not provided)
   - Meaning: (not provided, set @QuoteMeaningIntentionallyLeftBlank = 1)
   - Tags: (not provided)
3. Execute stored procedure via PowerShell
4. Report: "✓ SUCCESS: Quote added successfully! Quote ID: 1234"
```

### Example 3: Detailed Quote with Context (Manual Mode)

```
User: "Add quote with full details"

Agent Actions:
1. Ask questions to gather:
   - Quote Content: "Stay hungry, stay foolish"
   - Author: "Steve Jobs"
   - Context: "Stanford Commencement Speech, 2005"
   - Meaning: "Keep learning and questioning conventional wisdom"
   - Tags: "inspiration|education|innovation"
   - Paraphrased: No
2. Execute stored procedure with all parameters
3. Report: "✓ SUCCESS: Quote added successfully! Quote ID: 1235"
```

### Example 4: Duplicate Detection

```
User: "Add: 'Stay hungry, stay foolish' by Steve Jobs"

Agent Actions:
1. Execute stored procedure
2. Stored procedure detects duplicate
3. Report: "⚠ DUPLICATE: This quote already exists. Existing Quote ID: 1235"
```

## SQL Server Configuration

### Connection String Formats

**SQL Server Authentication:**

```
Server=localhost;Database=Basics2025;User Id=YourUser;Password=YourPassword;
```

**Windows Integrated Authentication (Recommended):**

```
Server=localhost;Database=Basics2025;Integrated Security=true;
```

**Named Instance:**

```
Server=localhost\SQLEXPRESS;Database=Basics2025;User Id=YourUser;Password=YourPassword;
```

**Remote Server with Port:**

```
Server=192.168.1.100,1433;Database=Basics2025;User Id=YourUser;Password=YourPassword;
```

### Required Permissions

The database user needs:

- `EXECUTE` permission on `CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING`
- Optionally `SELECT` on the quotes table to verify insertions

Grant with:

```sql
GRANT EXECUTE ON CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING TO [YourUser];
```

### Dependencies

**PowerShell:**

- Built-in `System.Data.SqlClient` (included with .NET Framework)
- No additional packages required
- Works on Windows PowerShell 5.1+ and PowerShell 7+

## Quick Start Guide

1. **Setup configuration:**

   ```powershell
   Copy-Item db-config.example.json db-config.json
   # Edit db-config.json with your connection string
   ```

2. **Use the skill:**

   ```
   Type: /database-quote-insert
   Or say: "Add this quote to database: [your quote]"
   ```

3. **Provide quote details when prompted:**
   - Quote content (required)
   - Author (optional)
   - Context (optional)
   - Meaning (optional)
   - Tags (optional, pipe-separated)

4. **Review results:**
   - ✓ SUCCESS = New quote added
   - ⚠ DUPLICATE = Quote already exists

## Testing & Verification

After insert, verify the quote was added:

```sql
-- Get the most recent quote
SELECT TOP 1 *
FROM CMS.ContextQuotes
ORDER BY QuoteID DESC

-- Find quote by author
SELECT *
FROM CMS.ContextQuotes
WHERE QuoteAttributionName LIKE '%Steve Jobs%'

-- Get quote by ID (from output parameter)
SELECT *
FROM CMS.ContextQuotes
WHERE QuoteID = 1234
```

## Troubleshooting

### Common Issues

**"Could not find stored procedure"**

- Verify procedure exists: `SELECT * FROM sys.procedures WHERE name = 'ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING'`
- Check schema: Make sure it's `CMS.ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING` not just `ContextQuotes_INSERT_WITH_DUPLICATE_CHECKING`

**"Cannot insert NULL value"**

- Ensure QuoteContent is provided (required field)
- Check that all NOT NULL columns in the underlying table are covered by the stored procedure

**"Return value is NULL"**

- Stored procedure may have failed silently
- Check SQL Server error logs for details

**"Login failed for user"**

- Verify credentials in db-config.json
- Try Integrated Security if on same server
- Check user has permissions on database

## Future Enhancements

Possible expansions:

- Bulk insert multiple quotes from file/CSV
- Update existing quotes by ID
- Delete quotes by ID
- Search/query quotes by tags, author, content
- Export quotes to JSON/CSV
- View quote history/audit trail
- Connection string encryption/secure storage
- Schema validation before insert
