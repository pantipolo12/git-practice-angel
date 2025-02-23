# Pokemon Card Storage Web App - Planning & Documentation

This document outlines the planning and design for the **Pokémon Card Storage Web App**,
using mermaid diagrams and markdown to represent key components of the system.


## Entity-Relationship Diagram (ERD)

```mermaid
erDiagram
    USER {
        int UserID
        String Username
        String Email
        String Password
        String Role
}

    CARD{
        int CardID
        String Name 
        String Type
        String Rarity
        int Attack
        int Defense
        int HP
        String Description
}
    DECK{
        int DeckID
        String DeckName
    }
    ADMIN {
        int AdminID
        String ApprovalStatus
}

USER ||--o| DECK : owns
DECK ||--o| CARD : contains
USER ||--o| ADMIN : hasRole
ADMIN ||--o| CARD : approves

```

## User Flow Diagram

```mermaid
flowchart TD
    A[User logs in] --> B{Is User an Admin?}
    B --> |Yes| C[Admin Dashboard]
    B --> |No| D[User Dashboard]
    
    D --> E[View Cards]
    D --> F[Submit New Card]
    D --> G[Manage Deck]

    F --> H[Pending approval by Admin]
    H --> |Approved| I[Card Visible]
    H --> |Denied| J[Card rejected]

    C --> K[Approve new cards]
    C --> L[Manage Cards]
    C --> M[Manage Users]
    
    E --> N[View card Details]
    G --> O[Create Deck]
    G --> P[Edit Deck]
    G --> Q[Remove cards from Deck]

```

## System Architecture Diagram

```mermaid
graph TD
    A[Frontend] --> B[API Server]
    B --> C[(Database)]
    B --> D[Authentication]
    D --> E[User Login]
    B --> F[Admin Dashboard]
    F --> G[Approve Cards]
    F --> H[Manage Cards]
    F --> I[Manage Users]
    E --> J[User Dashboard]
    J --> K[View Cards]
    J --> L[Manage Decks]
    K --> M[Card Details]
    L --> N[Add/Remove Cards]
```

## API Endpoints Table


## API Endpoints Table

| Endpoint                         | HTTP Method | Description                                  | Authentication/Authorization |
|----------------------------------|-------------|----------------------------------------------|------------------------------|
| `/cards`                         | GET         | Fetch all available cards                    | Public (No authentication)   |
| `/cards`                         | POST        | Submit a new card (pending admin approval)   | Authenticated (User Role)    |
| `/cards/{id}`                    | PUT         | Update card details (admin only)             | Authenticated (Admin Role)   |
| `/cards/{id}`                    | DELETE      | Delete a card (admin only)                   | Authenticated (Admin Role)   |
| `/decks`                         | GET         | Fetch all decks for the logged-in user       | Authenticated (User Role)    |
| `/decks`                         | POST        | Create a new deck                           | Authenticated (User Role)    |
| `/decks/{deckId}`                | PUT         | Edit a deck                                 | Authenticated (User Role)    |
| `/decks/{deckId}/cards`          | POST        | Add a card to a deck                        | Authenticated (User Role)    |
| `/decks/{deckId}/cards/{id}`     | DELETE      | Remove a card from a deck                   | Authenticated (Admin Role)   |


## User Strories
```mermaid
graph TD
    A[As a user, I want to view all Pokémon cards so I can see available cards] --> B[As a user, I want to create a deck so I can organize my cards]
    B --> C[As a user, I want to add cards to a deck so I can build a strategy]
    C --> D[As a user, I want to remove cards from a deck so I can adjust my deck]
    D --> E[As a user, I want to submit a new card so I can contribute to the collection]
    E --> F[As an admin, I want to approve new cards so that only valid cards are shown]
    F --> G[As an admin, I want to delete cards so I can remove inappropriate content]

```



## Requirement List

```mermaid
graph LR
    
    A[Need to Have] --> B[Card Viewing: Users can view all cards]
    A --> C[Deck Building: Users can create, edit, and remove decks]
    A --> D[Card Submission: Users can submit new cards 'pending admin approval']
    A --> E[Role-Based Permissions: Admins can approve, modify, and delete cards]
    
    F[Nice to Have] --> G[Card Search: Users can search cards by name/type]
    F --> H[Filtering by Type: Users can filter cards by type 'e.g., fire, water']
    F --> I[Deck Sharing: Users can share decks with others]
    F --> J[Deck Stats: Users can view deck statistics e.g., attack/defense ratings]

```