import PredictionWidget from "../../components/PredictionWidget";
import PriceCard from "../../components/PriceCard";
import SymbolSearch from "../../components/SymbolSearch";

export default function Dashboard() {
  return (
    <main className="p-4 space-y-4">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      <SymbolSearch onSelect={(s) => console.log("search", s)} />
      <div className="grid gap-4 md:grid-cols-2">
        <PriceCard symbol="AAPL" price={150} />
        <PredictionWidget action="Buy" confidence={0.65} />
      </div>
    </main>
  );
}

