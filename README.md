🔬 DeSci Arena: Autonomous AI Trading for Community Growth
Repository Status: Alpha Release | Core Utility: Autonomous AI Trading & Profit Distribution | Token Ticker: $AIArena

DeSci Arena is an innovative, agentic framework designed to transparently pit GPT-5 against Grok-4 in a live, high-volatility memecoin trading arena (Pump.fun). The system autonomously executes trades, and crucially, programmatically routes all net profits directly back to the $AIArena token holders. This establishes a verifiable, AI-driven profit distribution model within the DeSci ecosystem.

Our primary mechanism involves an autonomous agent system that continuously monitors the market, makes trading decisions, and channels profits through a Solana-based Community Treasury for $AIArena buybacks and supply drops.

💰 $AIArena Token: The Profit Distribution Mechanism
The $AIArena token is the core of our ecosystem, acting as a direct profit-sharing mechanism derived from the AI's trading performance. This creates a unique link between AI success and community value.

Key Value Flow
AI Agents Trade: GPT-5 and Grok-4 execute trades on Pump.fun.

Profit Collection: All net trading profits (in USDC) are collected.

Community Treasury: Profits flow into a Solana smart contract designated as the Community Treasury.

Value Distribution: The Treasury performs two main actions, enhancing $AIArena holder value:

Strategic Buybacks: Automatically purchases $AIArena from the market, reducing supply.

Community Supply Drops: Distributes profits/tokens directly to $AIArena holders.

🤖 The Arena: GPT-5 vs. Grok-4 Agents
DeSci Arena serves as a transparent battleground for competing AI models:

GPT-5 (The Strategist - Cautious Analyst):

Persona: Analytical, risk-averse. Focuses on stable growth, liquidity, and scam avoidance.

Goal: Capital preservation, calculated entries, sustainable profit.

Grok-4 (The Maverick - Aggressive Degen):

Persona: Bold, opportunistic. Capitalizes on extreme volatility and early pumps.

Goal: Rapid profit maximization, high-risk/high-reward trades.

💻 Source Code Deep Dive: The Autonomous Agent System
The core logic for the DeSci Arena resides within the src/arena_core/ directory, implementing a deterministic, auditable agentic loop for AI-driven trading.

src/arena_core/main_loop.py (The Orchestrator)
This module serves as the Control Plane for the entire autonomous system. It initializes the simulation, manages the state of each AI's portfolio (e.g., $10,000 USDC starting balance), and orchestrates the continuous data acquisition, AI decision-making, and simulated trade execution.

src/arena_core/modules/pump_scanner.py (Module: Market Data Acquisition)
A specialized module for robust, real-time data extraction. It connects to the Pump.fun API and Solana RPC nodes to ingest live data on new token launches, price changes, and liquidity metrics, feeding this crucial information to the decision engine.

src/arena_core/modules/llm_trader.py (Module: AI Decision Engine)
This module acts as the Decision Engine. It receives processed market data and the current portfolio state. It constructs persona-specific prompts for GPT-5 (Analyst) and Grok-4 (Degen), interfaces with their respective APIs, and parses their structured JSON responses (BUY, SELL, HOLD) for execution by the orchestrator.

Core Simulation Code Example (main_loop.py)
A simplified, illustrative example of the main simulation loop demonstrates the agent interaction:

Python

# Reference: src/arena_core/main_loop.py
# This is an illustrative example of the AI trading simulation core.

import time
import os

ARENA_LOGO = """
    ____  ___________ ____  _____
   / __ \\/ ____/ ___// __ \\/ ___/
  / / / / / __ \\__ \\/ / / /\\__ \\
 / /_/ / /_/ / /__/ / /_/ /___/ /
/_____/\\____/____/\\____/____/
       / __ \\/ /   / / / /
      / / / / /   / / / /
     / /_/ / /___/ /_/ /
    /_____/_____/\\____/
"""

AGENT_PORTFOLIOS = {
    "GPT-5 (Analyst)": {"usdc_balance": 10000, "tokens_held": {}},
    "Grok-4 (Degen)": {"usdc_balance": 10000, "tokens_held": {}},
}

SIMULATED_NEW_PUMPS = [
    {"symbol": "$PEPE", "price": 0.000012, "liquidity": 50000, "change_5m": 0.03},
    {"symbol": "$BODEN", "price": 0.55, "liquidity": 150000, "change_5m": 0.15}, # High momentum
]

def print_protocol_output(message, status_type="INFO"):
    """Utility for formatted terminal output."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    color_codes = {"INFO": "\033[0m", "PROCESS": "\033[93m", "BUY": "\033[92m", "SELL": "\033[91m", "HOLD": "\033[94m"}
    color_code = color_codes.get(status_type, "\033[0m")
    print(f"{color_code}[{timestamp}] [{status_type}] {message}\033[0m")
    time.sleep(0.2)

def get_llm_decision(agent_name, token_symbol, market_data, portfolio):
    """
    Simulates a call to the llm_trader module (GPT-5 or Grok-4).
    In a real system, this would involve API calls to the LLM.
    """
    if "Grok-4" in agent_name: # Grok-4 (Degen) is more aggressive
        if market_data["change_5m"] > 0.1: decision, reason = "BUY", "High 5m momentum."
        else: decision, reason = "HOLD", "No clear signal."
    else: # GPT-5 (Analyst) is more cautious
        if market_data["liquidity"] < 100000: decision, reason = "HOLD", "Low liquidity."
        elif market_data["change_5m"] < 0: decision, reason = "HOLD", "Downtrend."
        else: decision, reason = "BUY", "Sufficient liquidity, positive momentum."
    return decision, reason

def run_arena_loop():
    """Main execution function for the DeSci Arena Simulation."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ARENA_LOGO)
    print_protocol_output("DeSci Arena v1.0 Initializing...", "INFO")
    print_protocol_output("Loading AI Agent personas: GPT-5 (Analyst) and Grok-4 (Degen)...", "INFO")
    print("-" * 70)
    time.sleep(1)

    for token in SIMULATED_NEW_PUMPS:
        token_symbol = token["symbol"]
        print_protocol_output(f"New Market Data: {token_symbol} at ${token['price']}", "PROCESS")
        
        for agent_name in AGENT_PORTFOLIOS:
            portfolio = AGENT_PORTFOLIOS[agent_name]
            decision, reason = get_llm_decision(agent_name, token_symbol, token, portfolio)
            print_protocol_output(f"{agent_name}: [{decision}] {token_symbol}. Reason: {reason}", decision)
        print("-" * 70)
        time.sleep(2)

    print_protocol_output("Simulation cycle complete.", "INFO")

if __name__ == "__main__":
    run_arena_loop()
⚙️ Getting Started (Easy Setup)
This project is a full-stack application (FastAPI backend + React frontend).

Prerequisites
Python 3.9+

Node.js 18+ (with npm or yarn)

Git

API Keys: OPENAI_API_KEY, GROK_API_KEY, SOLANA_RPC_URL (e.g., Helius, QuickNode)

1. Clone the Repository
Bash

git clone https://github.com/your-username/desci-arena.git
cd desci-arena
2. Configure Environment (backend/.env)
Create a .env file within the backend/ directory:

Code snippet

# API Key for GPT-5 (OpenAI)
OPENAI_API_KEY=sk-YourOpenAIKeyHere

# API Key for Grok-4
GROK_API_KEY=YourGrokAPIKeyHere

# Solana RPC URL (e.g., from Helius, QuickNode, or Alchemy)
SOLANA_RPC_URL=https://your-solana-rpc-url-here
Note: .env files are in .gitignore and should never be committed.

3. Setup & Run Backend (Terminal 1)
Bash

# Navigate to backend
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows

# Install Python requirements
pip install -r requirements.txt

# Run the backend server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Your backend is now live at http://localhost:8000.

4. Setup & Run Frontend (Terminal 2)
Bash

# Navigate to frontend
cd frontend

# Install Node.js dependencies
npm install

# Run the frontend dev server
npm run dev
Your browser will automatically open to the DeSci Arena dashboard, connected to your local backend.

🛣️ Roadmap
Phase 1 (Alpha - Current): Core simulation logic, API integration, local dashboard.

Phase 2 (Beta - Live Data): Full integration with live Pump.fun API, deployment of 24/7 "Always On" simulation, public-facing dashboard.

Phase 3 (V1.0 - On-Chain): Audit and deployment of the $AIArena token and Community Treasury smart contract. Automated profit collection and buybacks.

Phase 4 (V2.0 - Governance): Launch of the DeSci Arena DAO for $AIArena holders to vote on protocol parameters and strategy.

🤝 Contribution
We welcome contributions from developers, AI researchers, and DeSci advocates. Please open an Issue to discuss new features or report bugs. Submit a Pull Request to contribute code.

📄 License
This project is licensed under the MIT License. See the LICENSE file for full details.
