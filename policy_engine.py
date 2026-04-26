import json
import sys

def validate_access_policy(file_path):
    with open(file_path, 'r') as file:
        policy = json.load(file)

    actions = policy.get("Action", [])
    if isinstance(actions, str):
        actions = [actions]
        
    for action in actions:
        if action == "*":
            return False # Blocked: Violates Least Privilege
            
    return True # Allowed: Secure

if __name__ == "__main__":
    target_file = sys.argv[1]
    print(f"--- Pipeline Security Scan: {target_file} ---")
    
    if validate_access_policy(target_file):
        print("[SUCCESS] Least Privilege validated. Access Granted.\n")
        sys.exit(0) # Tells GitHub Actions: PASS (Green Checkmark)
    else:
        print("[BLOCKED] Security Violation! Wildcard '*' access detected.")
        print("          Deployment stopped to prevent large-scale data breach.\n")
        sys.exit(1) # Tells GitHub Actions: FAIL (Red X - pipeline stops!)