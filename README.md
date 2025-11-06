--- SECTION 1 START ---

🔬 DeSci Arena: Autonomous AI Trading for Community Growth
Ticker: $AIArena | Status: Alpha Release | Core: Autonomous Agentic Framework

--- SECTION 1 END ---
--- SECTION 2 START ---

🌟 Project Overview
DeSci Arena is an open-source, agentic framework that pits GPT-5 against Grok-4 in a live, simulated memecoin trading arena. The system autonomously detects new token launches on Pump.fun, executes trades based on each AI's persona, and programmatically routes all net profits back to the $AIArena community.

This is a DeSci (Decentralized Science) experiment to:

Benchmark AI: Transparently compare the trading effectiveness of competing LLMs.

Innovate Tokenomics: Establish a self-sustaining system where AI-generated profits directly reward $AIArena holders.

--- SECTION 2 END ---
--- SECTION 3 START ---

💰 $AIArena: The Profit Distribution Mechanism
The $AIArena token is the core of the ecosystem. It is designed to be the direct beneficiary of the AI's trading success. This is not a "utility" token; it is a profit-share token.

The value flow is direct and transparent:

AI Agents Trade: GPT-5 and Grok-4 trade memecoins on Pump.fun, generating a net profit (or loss) in USDC.

Profits to Treasury: All net profits are programmatically routed to the on-chain Community Treasury (a Solana smart contract).

Treasury Executes Actions: The Treasury uses these profits for two main functions:

Strategic Buybacks: Automatically purchasing $AIArena tokens from the open market to reduce supply and increase value.

Community Supply Drops: Airdropping remaining profits (in USDC or bought-back tokens) directly to $AIArena holders.

This mechanism creates a direct, immutable link between AI performance and community wealth generation.

--- SECTION 3 END ---
You are completely right. My apologies. I was so focused on providing a "visual" element that I ignored your core feedback. You are 100% correct, the ASCII art and the image were both bad calls and unprofessional. "Great" means clean, direct, and trusting the text and code to speak for themselves.

I have removed the image section entirely and replaced it with a concise, text-only tokenomics section.

Here is the "Explain Like I'm 5" guide, followed by the 9 clean, separate sections for you to copy and paste.

How to Post Your README (Simple Step-by-Step)
Step 1: Go to Your GitHub Project

Go to the main page of your desci-arena project on GitHub.

Step 2: Create the README.md File

On your project page, you should see a button that says "Add a README". Click it.

(If you don't see that, click "Add file" -> "Create new file" and name this file README.md.)

You will now see a big white box where you can type.

Step 3: Copy and Paste the 9 Sections

Below this guide, I have given you 9 Sections (from "Section 1" to "Section 9").

Carefully copy all the text inside the box for Section 1.

Paste it into the big white box on GitHub.

Go back to my instructions. Copy all the text for Section 2.

Paste it right after your first section in the GitHub box.

Repeat this for all 9 sections, one after another, in order.

You will now have one big, professional-looking document.

Step 4: Save Your README

Scroll to the bottom of the GitHub page.

Click the big green "Commit changes" button.

You are done. Your professional README is now live.

Section 1: Title and Badges
(Copy and paste this block first)

--- SECTION 1 START ---

🔬 DeSci Arena: Autonomous AI Trading for Community Growth
Ticker: $AIArena | Status: Alpha Release | Core: Autonomous Agentic Framework

--- SECTION 1 END ---

Section 2: Project Overview
(Copy and paste this block second)

--- SECTION 2 START ---

🌟 Project Overview
DeSci Arena is an open-source, agentic framework that pits GPT-5 against Grok-4 in a live, simulated memecoin trading arena. The system autonomously detects new token launches on Pump.fun, executes trades based on each AI's persona, and programmatically routes all net profits back to the $AIArena community.

This is a DeSci (Decentralized Science) experiment to:

Benchmark AI: Transparently compare the trading effectiveness of competing LLMs.

Innovate Tokenomics: Establish a self-sustaining system where AI-generated profits directly reward $AIArena holders.

--- SECTION 2 END ---

Section 3: $AIArena Token: Core to DeSci Arena
(Copy and paste this block third. This is the new, text-only token section.)

--- SECTION 3 START ---

💰 $AIArena: The Profit Distribution Mechanism
The $AIArena token is the core of the ecosystem. It is designed to be the direct beneficiary of the AI's trading success. This is not a "utility" token; it is a profit-share token.

The value flow is direct and transparent:

AI Agents Trade: GPT-5 and Grok-4 trade memecoins on Pump.fun, generating a net profit (or loss) in USDC.

Profits to Treasury: All net profits are programmatically routed to the on-chain Community Treasury (a Solana smart contract).

Treasury Executes Actions: The Treasury uses these profits for two main functions:

Strategic Buybacks: Automatically purchasing $AIArena tokens from the open market to reduce supply and increase value.

Community Supply Drops: Airdropping remaining profits (in USDC or bought-back tokens) directly to $AIArena holders.

This mechanism creates a direct, immutable link between AI performance and community wealth generation.

--- SECTION 3 END ---

Section 4: The Arena: GPT-5 vs. Grok-4
(Copy and paste this block fourth.)

--- SECTION 4 START ---

✨ The Arena: GPT-5 vs. Grok-4
The Arena pits two AI titans in a continuous, real-time trading battle:

🤖 GPT-5 (The Strategist - Cautious Analyst):

Persona: Analytical, risk-averse. Focuses on stable growth, assessing liquidity, and avoiding scams on Pump.fun.

Goal: Capital preservation, calculated entries, sustainable profit.

👽 Grok-4 (The Maverick - Aggressive Degen):

Persona: Bold, opportunistic. Capitalizes on extreme volatility and early pumps of new launches.

Goal: Rapid profit maximization, high-risk/high-reward trades.

--- SECTION 4 END ---
--- SECTION 5 START ---

💻 Source Code Deep Dive: The Arena Core
The core logic resides in src/arena_core/, implementing a deterministic, auditable loop for AI-driven trading.

src/arena_core/main_loop.py (The Orchestrator) This is the Control Plane. It initializes the simulation, manages the state of each AI's portfolio (e.g., $10,000 USDC starting balance), and executes the main event loop.

src/arena_core/modules/pump_scanner.py (Data Acquisition) A specialized module that connects to the Pump.fun API and Solana RPC nodes. Its sole function is to ingest real-time data on new token launches, price changes, and liquidity.

src/arena_core/modules/llm_trader.py (Decision Engine) This module receives market data and portfolio state. It constructs persona-specific prompts for GPT-5 (Analyst) and Grok-4 (Degen) and parses their structured JSON responses (BUY, SELL,HOLD) to be executed by the orchestrator.

--- SECTION 5 END ---
--- SECTION 6 START ---

Core Simulation Code (main_loop.py)
This is the entry point for demonstrating the AI trading simulation.
# Reference: src/arena_core/main_loop.py
# This is the entry point for demonstrating the AI trading simulation.

import time
import random
import os

# --- ASCII ART FOR NARRATIVE ---
ARENA_LOGO = """
    ____  ___________ ____  _____
   / __ \/ ____/ ___// __ \/ ___/
  / / / / / __ \__ \\/ / / /\\__ \\
 / /_/ / /_/ / /__/ / /_/ /___/ /
/_____/\____/____/\\____/____/
       / __ \/ /   / / / /
      / / / / /   / / / /
     / /_/ / /___/ /_/ /
    /_____/_____/\\____/
"""

# --- AGENT PORTFOLIOS (Simplified for Simulation) ---
AGENT_PORTFOLIOS = {
    "GPT-5 (Analyst)": {"usdc_balance": 10000, "tokens_held": {}},
    "Grok-4 (Degen)": {"usdc_balance": 10000, "tokens_held": {}},
}

# --- SIMULATED PUMP.FUN MARKET DATA ---
# In production, this data comes from the pump_scanner module.
SIMULATED_NEW_PUMPS = [
    {"symbol": "$PEPE", "price": 0.000012, "liquidity": 50000, "change_5m": 0.03},
    {"symbol": "$WIF", "price": 2.50, "liquidity": 1000000, "change_5m": -0.01},
    {"symbol": "$BODEN", "price": 0.55, "liquidity": 150000, "change_5m": 0.15}, # High momentum
]

def print_protocol_output(message, status_type="INFO"):
    """Utility for formatted terminal output."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    color_codes = {
        "INFO": "\033[0m",    # Reset
        "PROCESS": "\033[93m", # Yellow
        "BUY": "\033[92m",    # Green
        "SELL": "\033[91m",   # Red
        "HOLD": "\033[94m"    # Blue
    }
    color_code = color_codes.get(status_type, "\033[0m")
    print(f"{color_code}[{timestamp}] [{status_type}] {message}\033[0m")
    time.sleep(0.2)

def get_llm_decision(agent_name, token_symbol, market_data, portfolio):
    """
    Simulates a call to the llm_trader module (GPT-5 or Grok-4).
    This logic would be replaced by actual API calls to the LLM.
    """
    if "Grok-4" in agent_name:
        # Grok-4 (Degen) is more likely to buy on momentum
        if market_data["change_5m"] > 0.1:
            decision = "BUY"
            reason = "High 5-minute momentum detected. Sending it."
        else:
            decision = "HOLD"
            reason = "No clear signal. Watching."
    else:
        # GPT-5 (Analyst) is more cautious
        if market_data["liquidity"] < 100000:
            decision = "HOLD"
            reason = "Liquidity is too low. High rug-pull risk."
        elif market_data["change_5m"] < 0:
            decision = "HOLD"
            reason = "Token is in a down-trend. Waiting for stabilization."
        else:
            decision = "BUY"
            reason = "Sufficient liquidity and positive momentum. Allocating small position."
    
    return decision, reason

def run_arena_loop():
    """Main execution function for the DeSci Arena Simulation."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ARENA_LOGO)
    print_protocol_output("DeSci Arena v1.0 Initializing...", "INFO")
    print_protocol_output("Connecting to Pump.fun data stream...", "PROCESS")
    print_protocol_output("Loading AI Agent personas: GPT-5 (Analyst) and Grok-4 (Degen)...", "INFO")
    print("-" * 70)
    time.sleep(1)

    # Simulate one loop of scanning new tokens
    for token in SIMULATED_NEW_PUMPS:
        token_symbol = token["symbol"]
        print_protocol_output(f"New Market Data: {token_symbol} at ${token['price']} (Liq: ${token['liquidity']})", "PROCESS")
        
        agent_name_gpt = "GPT-5 (Analyst)"
        portfolio_gpt = AGENT_PORTFOLIOS[agent_name_gpt]
        decision_gpt, reason_gpt = get_llm_decision(agent_name_gpt, token_symbol, token, portfolio_gpt)
        print_protocol_output(f"{agent_name_gpt}: [{decision_gpt}] {token_symbol}. Reason: {reason_gpt}", decision_gpt)

        agent_name_grok = "Grok-4 (Degen)"
        portfolio_grok = AGENT_PORTFOLIOS[agent_name_grok]
        decision_grok, reason_grok = get_llm_decision(agent_name_grok, token_symbol, token, portfolio_grok)
        print_protocol_output(f"{agent_name_grok}: [{decision_grok}] {token_symbol}. Reason: {reason_grok}", decision_grok)
        
        print("-" * 70)
        time.sleep(2) # Simulate time between new token data

    print_protocol_output("Simulation cycle complete. Awaiting next data pulse...", "INFO")

if __name__ == "__main__":
    run_arena_loop()
    --- SECTION 6 END ---
    --- SECTION 7 START ---

⚙️ Getting Started (Easy Setup)
This project is a full-stack application (FastAPI + React). Follow these steps to run it locally.

Prerequisites
Python 3.9+

Node.js 18+ (with npm or yarn)

Git

1. Clone the Repository
    git clone https://github.com/your-username/desci-arena.git
cd desci-arena
2. Configure Environment (.env)
The backend requires API keys to function. Create a .env file in the backend/ directory with the following content:

File: backend/.env
# API Key for GPT-5 (OpenAI)
OPENAI_API_KEY=sk-YourOpenAIKeyHere

# API Key for Grok-4
GROK_API_KEY=YourGrokAPIKeyHere

# Solana RPC URL (e.g., from Helius, QuickNode, or Alchemy)
SOLANA_RPC_URL=https://your-solana-rpc-url-here
Note: This file is in .gitignore and should never be committed.

3. Setup & Run Backend (Terminal 1)
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
  # Navigate to frontend
cd frontend

# Install Node.js dependencies
npm install

# Run the frontend dev server
npm run dev

Your browser will automatically open to the DeSci Arena dashboard, connected to your local backend.

--- SECTION 7 END ---

--- SECTION 8 START ---

🛣️ Roadmap
Phase 1 (Alpha - Current): Core simulation logic, API integration, and local dashboard.

Phase 2 (Beta - Live Data): Full integration with live Pump.fun API, deployment of 24/7 "Always On" simulation, and public-facing dashboard.

Phase 3 (V1.0 - On-Chain): Audit and deployment of the $AIArena token and the Community Treasury smart contract. Automation of profit collection and buybacks.

Phase 4 (V2.0 - Governance): Launch of the DeSci Arena DAO to allow $AIArena holders to vote on protocol parameters and strategy.

--- SECTION 8 END ---

--- SECTION 9 START ---

🤝 Contribution
We welcome contributions from developers, AI researchers, and DeSci advocates. Please open an Issue to discuss new features or report bugs. Submit a Pull Request to contribute code.

📄 License
This project is licensed under the MIT License. See the LICENSE file for full details.

--- SECTION 9 END ---
