import pandas as pd
import neurokit2 as nk

class CardioPhyMLEngine:
    def analyze(self, ecg_file: str, sampling_rate: int = 250):
        df = pd.read_csv(ecg_file)
        # Auto-detect ECG column
        ecg_col = None
        for col in ['ecg', 'lead_II', 'ECG', 'signal']:
            if col in df.columns:
                ecg_col = col
                break
        if ecg_col is None:
            raise ValueError("Expected ECG column not found. Use 'ecg', 'lead_II', etc.")
        
        ecg_signal = df[ecg_col].values
        clean_ecg = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)
        _, rpeaks = nk.ecg_peaks(clean_ecg, sampling_rate=sampling_rate)
        hrv = nk.hrv_time(rpeaks, sampling_rate=sampling_rate)

        rr_intervals = rpeaks["ECG_R_Peaks"][1:] - rpeaks["ECG_R_Peaks"][:-1]
        hr = 60 / (rr_intervals.mean() / sampling_rate)
        rmssd = hrv["HRV_RMSSD"].iloc[0] if not hrv.empty else 20.0

        # Simple risk proxy (lower RMSSD + high HR → higher risk)
        risk_score = max(0, min(100, 70 - (rmssd / 50) * 20 + (hr - 70) * 0.8))

        return {
            "heart_rate_bpm": float(hr),
            "hrv_rmssd_ms": float(rmssd),
            "risk_score": float(risk_score),
            "message": f"Cardiovascular risk estimate: {risk_score:.1f}/100"
        }