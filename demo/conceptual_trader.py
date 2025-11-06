import time
import random

# --- Simulated AI "Brains" ---
# In a real app, these functions would make API calls to a fine-tuned LLM.
# Here, we simulate their different "personalities" with simple logic.

def llm_agent_alpha(token_info):
    """
    Simulates "Agent Alpha," a more aggressive, risk-on trader.
    It favors very low market caps and high-buzz keywords.
    """
    # Simulate a "decision" based on the token's data
    if token_info['market_cap'] < 5000 and "dog" in token_info['name'].lower():
        return "BUY"
    
    if token_info['liquidity_percent'] > 0.8: # Checks if most of the initial LP is locked/burned
        return "BUY"

    return "PASS"

def llm_agent_omega(token_info):
    """
    Simulates "Agent Omega," a more cautious, analytical trader.
    It dislikes "risky" names and prefers slightly more established tokens.
    """
    # Simulate a different decision-making process
    if "safe" in token_info['name'].lower() or "moon" in token_info['name'].lower():
        return "PASS" # Considers these "scam" words

    if token_info['market_cap'] > 7500 and token_info['liquidity_percent'] > 0.7:
        return "BUY" # Prefers to buy after the initial chaos

    return "PASS"

# --- Simulated Market Monitor ---
# In a real app, this would use a WebSocket or API to get
# real-time data from pump.fun or another on-chain source.

def mock_fetch_new_tokens():
    """
    Simulates a new token being created on pump.fun.
    """
    token_names = ["Super Doge", "Cat Wif Hat", "SafeMoon v9", "Pepe Classic", "Mega Dog", "Quantum Sol"]
    
    token = {
        "name": f"{random.choice(token_names)}",
        "ticker": f"${''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))}",
        "market_cap": random.randint(1000, 20000), # Simulates initial market cap
        "liquidity_percent": random.uniform(0.5, 1.0) # Simulates % of tokens in LP
    }
    return token

# --- Main Arena Loop ---

def run_arena_simulation():
    """
    Runs the main simulation loop for the Desci Arena.
    """
    print("--- ⚔️ Welcome to the Desci Arena ($AIArena) Simulation ⚔️ ---")
    print("Two AI agents will now compete to trade new memecoins.")
    print("Press CTRL+C to stop the simulation.\n")
    
    try:
        while True:
            # 1. A new token appears
            new_token = mock_fetch_new_tokens()
            print("---------------------------------------------------------")
            print(f"🚀 New Token Detected!")
            print(f"   Name: {new_token['name']} ({new_token['ticker']})")
            print(f"   Market Cap: ${new_token['market_cap']}")
            print(f"   Liquidity %: {new_token['liquidity_percent']:.1%}\n")

            # 2. Both AIs analyze the token
            print("🧠 Agents are analyzing...")
            time.sleep(1) # Simulate network/processing time
            
            decision_alpha = llm_agent_alpha(new_token)
            decision_omega = llm_agent_omega(new_token)

            # 3. Print the results
            print(f"   🤖 Agent Alpha Decision: {decision_alpha}")
            print(f"   🤖 Agent Omega Decision: {decision_omega}\n")

            # Wait for the next token
            time.sleep(4) # Simulate time between new token launches

    except KeyboardInterrupt:
        print("\n--- Simulation Stopped ---")
        print("Profits (if any) would now be calculated and distributed.")

if __name__ == "__main__":
    run_arena_simulation()
