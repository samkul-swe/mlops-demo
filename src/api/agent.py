"""
AI Agent for Credit Analysis
Uses Claude to provide human-readable credit analysis
"""
import os
from typing import Dict, Any

try:
    from anthropic import Anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False


class CreditAnalystAgent:
    """AI agent that analyzes credit applications"""
    
    def __init__(self):
        self.client = None
        if HAS_ANTHROPIC and os.getenv("ANTHROPIC_API_KEY"):
            try:
                self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            except:
                pass
    
    def analyze(self, application: Dict[str, Any], prediction: Dict[str, Any]) -> str:
        """
        Generate AI-powered analysis of credit decision
        
        If API key not available, returns rule-based analysis
        """
        if not self.client:
            return self._rule_based_analysis(application, prediction)
        
        try:
            prompt = self._build_prompt(application, prediction)
            
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return message.content[0].text
        except:
            # Fallback to rule-based if API fails
            return self._rule_based_analysis(application, prediction)
    
    def _build_prompt(self, application: Dict, prediction: Dict) -> str:
        """Build prompt for Claude"""
        return f"""You are a credit analyst. Analyze this application briefly:

Application:
- Age: {application.get('age')}
- Income: ${application.get('annual_income'):,}
- Debt-to-Income: {application.get('debt_to_income_ratio'):.2f}
- Late Payments: {application.get('num_late_payments')}
- Credit Utilization: {application.get('credit_utilization'):.0%}

Decision:
- Credit Score: {prediction.get('credit_score')}
- Recommendation: {prediction.get('approval_recommendation')}
- Terms: {prediction.get('recommended_terms', {}).get('term_months')} months at {prediction.get('recommended_terms', {}).get('apr')}% APR

Provide a 2-3 sentence professional analysis for the lending team."""

    def _rule_based_analysis(self, application: Dict, prediction: Dict) -> str:
        """Simple rule-based analysis when AI not available"""
        score = prediction.get('credit_score', 0)
        decision = prediction.get('approval_recommendation', 'UNKNOWN')
        dti = application.get('debt_to_income_ratio', 0)
        late_payments = application.get('num_late_payments', 0)
        
        if score >= 750:
            risk = "Prime borrower with strong credit profile."
        elif score >= 650:
            risk = "Near-prime borrower with acceptable risk."
        else:
            risk = "Subprime borrower requiring careful consideration."
        
        concerns = []
        if dti > 0.5:
            concerns.append("high debt-to-income ratio")
        if late_payments > 2:
            concerns.append("history of late payments")
        
        if concerns:
            return f"{risk} Note: {', '.join(concerns)}. Decision: {decision}."
        else:
            return f"{risk} No major risk factors identified. Decision: {decision}."
