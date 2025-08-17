interface Props {
  symbol: string;
  price: number;
}

/** Display a symbol with its latest price. */
export default function PriceCard({ symbol, price }: Props) {
  return (
    <div className="rounded border p-4 text-center">
      <div className="text-sm text-gray-500">{symbol}</div>
      <div className="text-2xl font-bold">{price.toFixed(2)}</div>
    </div>
  );
}

