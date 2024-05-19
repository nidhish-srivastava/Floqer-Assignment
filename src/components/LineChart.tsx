import React, { useMemo } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import jsondata from "../assets/csvjson.json";
import { JobDataType } from "../types";

const data = jsondata as JobDataType[]

const LineGraph: React.FC = () => {
  const aggregatedData = useMemo(() => {
    const yearMap: { [key: number]: number } = {};

    data.forEach((job: JobDataType) => {
      if (!yearMap[job.work_year]) {
        yearMap[job.work_year] = 0;
      }
      yearMap[job.work_year] += 1;
    });

    return Object.entries(yearMap)
      .map(([year, totalJobs]) => ({
        year: parseInt(year, 10),
        totalJobs,
      }))
      .filter((entry) => entry.year >= 2020 && entry.year <= 2024);
  }, []);

  return (
    <LineChart
      className="LineChart"
      width={800}
      height={400}
      data={aggregatedData}
      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="year" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line
        type="monotone"
        dataKey="totalJobs"
        stroke="#8884d8"
        activeDot={{ r: 8 }}
      />
    </LineChart>
  );
};

export default LineGraph;
