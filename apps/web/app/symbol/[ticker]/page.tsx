interface Props {
  params: { ticker: string };
}

export default function SymbolPage({ params }: Props) {
  return <div>Symbol: {params.ticker}</div>;
}
