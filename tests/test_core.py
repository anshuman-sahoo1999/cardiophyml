# tests/test_core.py
import os
import pytest
from cardiophyml import CardioPhyMLEngine

def test_analyze_sample_ecg():
    """Test analysis on included sample ECG."""
    engine = CardioPhyMLEngine()
    file_path = os.path.join("examples", "sample_ecg.csv")
    result = engine.analyze(file_path)
    
    # Check keys exist
    assert "heart_rate_bpm" in result
    assert "hrv_rmssd_ms" in result
    assert "risk_score" in result
    
    # Check values are reasonable
    assert 50 < result["heart_rate_bpm"] < 100
    assert 0 <= result["risk_score"] <= 100