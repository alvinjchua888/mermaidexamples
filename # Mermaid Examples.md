# Mermaid Examples

This repository contains examples of [Mermaid](https://mermaid.js.org/) diagrams. Mermaid is a JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions to create and modify diagrams dynamically.

## What is Mermaid?

Mermaid allows you to create diagrams and visualizations using text and code. It's widely supported in documentation platforms like GitHub, GitLab, and many static site generators.

## Examples

### Flowchart

Basic flowchart showing a simple decision process:

```mermaid
flowchart TD
    A[Start] --> B{Is it working?}
    B -- Yes --> C[Continue]
    B -- No --> D[Fix it]
    D --> B
```

### Sequence Diagram

Shows interactions between different actors over time:

```mermaid
sequenceDiagram
    participant User
    participant App
    participant Database
    
    User->>App: Login request
    App->>Database: Validate credentials
    Database-->>App: User data
    App-->>User: Login successful
```

### Git Graph

Visualizes git branching and merging:

```mermaid
gitgraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
```

### Class Diagram

Shows relationships between classes:

```mermaid
classDiagram
    class Animal {
        +String name
        +String species
        +makeSound()
    }
    
    class Dog {
        +String breed
        +bark()
    }
    
    class Cat {
        +String color
        +meow()
    }
    
    Animal <|-- Dog
    Animal <|-- Cat
```

### State Diagram

Represents state transitions:

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Loading : start
    Loading --> Success : data received
    Loading --> Error : request failed
    Success --> Idle : reset
    Error --> Idle : retry
    Error --> [*] : exit
```

### Gantt Chart

Project timeline visualization:

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Planning
    Requirements    :done, req, 2024-01-01, 2024-01-15
    Design         :done, design, after req, 10d
    section Development
    Frontend       :active, frontend, 2024-01-20, 20d
    Backend        :backend, after design, 15d
    section Testing
    Unit Tests     :testing, after frontend, 5d
    Integration    :integration, after backend, 7d
```

## How to Use

1. **In GitHub/GitLab**: Simply add mermaid code blocks in your markdown files
2. **In VS Code**: Install the "Mermaid Preview" extension
3. **In documentation sites**: Most modern static site generators support Mermaid
4. **Online**: Use the [Mermaid Live Editor](https://mermaid.live) to create and test diagrams

## Syntax Resources

- [Official Mermaid Documentation](https://mermaid.js.org/)
- [Flowchart Syntax](https://mermaid.js.org/syntax/flowchart.html)
- [Sequence Diagram Syntax](https://mermaid.js.org/syntax/sequenceDiagram.html)
- [Class Diagram Syntax](https://mermaid.js.org/syntax/classDiagram.html)
- [State Diagram Syntax](https://mermaid.js.org/syntax/stateDiagram.html)
- [Gantt Chart Syntax](https://mermaid.js.org/syntax/gantt.html)

## Tips

- Use meaningful names for nodes and connections
- Keep diagrams simple and focused
- Use consistent styling and naming conventions
- Test your diagrams in the Mermaid Live Editor before committing
- Consider the audience when choosing diagram types

## Contributing

Feel free to add more examples or improve existing ones. Make sure to:
- Test diagrams before submitting
- Add clear descriptions for complex diagrams
- Follow the existing structure and formatting