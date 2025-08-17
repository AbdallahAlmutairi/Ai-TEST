interface Props {
  action: string;
  confidence: number;
}

/** Present the latest model prediction in a small card. */
export default function PredictionWidget({ action, confidence }: Props) {
  return (
    <div className="rounded border p-4 text-center">
      <div className="text-sm text-gray-500">Model Suggests</div>
      <div className="text-xl font-semibold">{action}</div>
      <div className="text-sm text-gray-500">
        Confidence: {(confidence * 100).toFixed(1)}%
      </div>
    </div>
  );
}

