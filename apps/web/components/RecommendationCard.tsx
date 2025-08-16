import React from "react";

interface Props {
  ticker: string;
  rating: string;
}

export default function RecommendationCard({ ticker, rating }: Props) {
  return (
    <div>
      {ticker}: {rating}
    </div>
  );
}
