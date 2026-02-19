# Multi-Agent Travel Planner using Google ADK

## 📖 Overview

This project is a Multi-Agent Travel Planner built using Google ADK (Agent Development Kit).

The system demonstrates agent orchestration using:
- 1 Root Agent (Orchestrator)
- 3 Specialized Sub-Agents
- Built-in google_search tool
- 3 Custom Tools

The goal is to simulate a travel planning workflow including flights, hotels, activities, and cost optimization.

---

## 🎯 Problem Statement

Planning a trip requires checking flights, comparing hotels, selecting activities, and managing budget constraints. This process is time-consuming and fragmented across platforms.

This system automates travel planning using multiple AI agents that collaborate to:

- Suggest flights
- Recommend hotels
- Plan activities
- Calculate total cost
- Generate structured itinerary output

---

## 🏗 Architecture

### 🔹 Root Agent (travel_planner_root)
- Orchestrates entire workflow
- Delegates tasks to sub-agents
- Combines responses
- Uses tools for cost calculation and search

### 🔹 Sub-Agents

1. **Flight Agent**
   - Finds flight options
   - Uses google_search

2. **Hotel Agent**
   - Suggests hotels within budget
   - Uses google_search

3. **Activity Agent**
   - Plans daily activities
   - Uses google_search

---

## 🛠 Tools Used

### ✅ Built-in Tool (Mandatory)
- `google_search`

### ✅ Custom Tools

1. `calculate_total_cost(flight_price, hotel_price, activity_cost)`
   - Computes total trip cost

2. `check_schedule_conflict(itinerary)`
   - Validates schedule conflicts

3. `generate_itinerary_report(destination, total_cost, details)`
   - Generates formatted Markdown itinerary

---

## ⚙️ Agent Pattern Used

Sequential Pattern:

User Request  
→ Root Agent  
→ Flight Agent  
→ Hotel Agent  
→ Activity Agent  
→ Cost Tool  
→ Final Structured Output  

---


