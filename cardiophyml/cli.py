# cardiophyml/cli.py
import argparse
import sys
import os
from .core import CardioPhyMLEngine

def main():
    parser = argparse.ArgumentParser(
        description="CardioPhyML: Physics-informed cardiovascular risk assessment from ECG data."
    )
    parser.add_argument(
        "--file", "-f",
        type=str,
        help="Path to ECG CSV file (must contain 'time' and 'lead_II' or 'ecg' column)"
    )
    args = parser.parse_args()

    # If no file provided, prompt user
    if args.file is None:
        print("🚀 CardioPhyML: Cardiovascular Risk Analyzer")
        print("Please provide an ECG file for analysis.")
        file_path = input("Enter path to ECG CSV file: ").strip()
    else:
        file_path = args.file

    # Validate file
    if not os.path.isfile(file_path):
        print(f"❌ Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        engine = CardioPhyMLEngine()
        result = engine.analyze(file_path)
        print("\n✅ Analysis Complete!")
        print(f"• Heart Rate: {result['heart_rate_bpm']:.1f} BPM")
        print(f"• HRV (RMSSD): {result['hrv_rmssd_ms']:.1f} ms")
        print(f"• Risk Score: {result['risk_score']:.1f}/100")
        print(f"\n💡 {result['message']}")
    except Exception as e:
        print(f"❌ Analysis failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()