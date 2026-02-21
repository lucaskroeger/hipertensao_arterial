# 🫀 Hypertension Awareness Game

An educational game developed in Python to simulate the long-term impact
of lifestyle choices on arterial hypertension.

This project was created as a university challenge to raise awareness
about hypertension through interactive decision-making. Instead of
delivering a traditional presentation, we engineered a modular game
system that translates medical concepts into gameplay mechanics.

------------------------------------------------------------------------

## 🎯 Purpose

The main goals of this project are:

-   Raise awareness about arterial hypertension\
-   Demonstrate how daily habits influence long-term health\
-   Apply software engineering best practices in a non-traditional
    domain\
-   Showcase modular architecture and design pattern usage in Python

------------------------------------------------------------------------

## 🧠 Concept

Players must manage lifestyle decisions that directly impact blood
pressure and overall health.

Throughout the game, the player interacts with elements representing:

-   🥗 Healthy and unhealthy food\
-   😰 Stress factors\
-   🏃 Physical activity\
-   💊 Medication adherence

Each decision dynamically affects health metrics and overall score,
reinforcing cause-and-effect learning over time.

------------------------------------------------------------------------

## 🏗️ Architecture Overview

The project was intentionally designed with separation of concerns and
modular structure.

    main.py
    game/
     ├── player.py
     ├── phase.py
     ├── element.py
     ├── level_selector.py
     ├── settings.py
     ├── render/
     │    ├── render_factory.py
     │    ├── render_time.py
     │    ├── render_heart.py
     └── score/
          ├── score_service.py
          ├── best_scores-*.json
    images/

------------------------------------------------------------------------

## 🧩 Design Patterns & Engineering Practices

### ✔ Separation of Concerns

-   Game logic separated from rendering logic\
-   Score management isolated in a service layer\
-   Clear modular responsibility boundaries

### ✔ Factory Pattern

-   `render_factory.py` centralizes rendering strategy creation\
-   Enables extensibility and flexible rendering components

### ✔ Service Layer Pattern

-   `score_service.py` encapsulates ranking and persistence logic\
-   Prevents tight coupling between gameplay and storage

### ✔ Object-Oriented Design

-   Encapsulated player behavior\
-   Element abstraction\
-   Phase/state management

### ✔ Persistence Layer

-   JSON-based score storage per difficulty level\
-   Decoupled from core game logic

------------------------------------------------------------------------

## ⚙️ Technical Details

-   Language: Python\
-   Architecture: Modular, OOP-based\
-   State-driven game loop\
-   Dynamic difficulty handling\
-   Ranking persistence system\
-   Extensible rendering structure

------------------------------------------------------------------------

## 🚀 What This Project Demonstrates

This project highlights the ability to:

-   Design modular systems beyond traditional web stacks\
-   Apply design patterns in practical scenarios\
-   Translate real-world problems into interactive systems\
-   Manage complexity using clean architecture principles\
-   Deliver complete end-to-end software solutions

Although game development is not my primary stack, this project reflects
strong engineering fundamentals that transfer directly to backend
systems, distributed architectures, and production environments.

------------------------------------------------------------------------

## ▶ How to Run

### 1. Clone the repository

    git clone <repository-url>

### 2. Navigate to the project directory

    cd hypertension-awareness-game

### 3. Install dependencies (if required)

    pip install -r requirements.txt

### 4. Run the game

    python main.py

------------------------------------------------------------------------

## 📌 Engineering Philosophy

Engineering is not about frameworks.

It is about:

-   Modeling systems\
-   Managing complexity\
-   Designing scalable structures\
-   Solving meaningful problems

This project represents that philosophy.
