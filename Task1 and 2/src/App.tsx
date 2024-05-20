import LineGraph from "./components/LineChart";
import Table from "./components/Table";

function App() {
  return (
    <>
    <div style={{margin: "2rem"}}>
    <h2 className="center">Main Table</h2>
    <Table/>
    </div>
      <div className="container center">
        <h2>Job Trends from 2020 to 2024</h2>
        <LineGraph />
      </div>
    </>
  );
}

export default App;
