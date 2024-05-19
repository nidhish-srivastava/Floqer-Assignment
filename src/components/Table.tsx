// src/JobTable.tsx
import React, { useState, useEffect } from "react";
import jsondata from "../assets/csvjson.json"; 
import { JobDataType } from "../types";

const data  = jsondata as JobDataType[]

type AggregatedData = {
  year: number;
  totalJobs: number;
  averageSalary: number;
};

type JobTitleData = {
  job_title: string;
  count: number;
};

const Table: React.FC = () => {
  const [aggregatedData, setAggregatedData] = useState<AggregatedData[]>([]);
  const [sortColumn, setSortColumn] = useState<keyof AggregatedData>("year");
  const [sortDirection, setSortDirection] = useState<"asc" | "desc">("desc");
  const [selectedYear, setSelectedYear] = useState<number | null>(null);
  const [jobTitles, setJobTitles] = useState<JobTitleData[]>([]);
  const [showTable, setShowTable] = useState(false);

  useEffect(() => {
    const aggregateDataHandler = () => {
      const yearMap: {
        [key: number]: { totalJobs: number; totalSalary: number };
      } = {};

      data.forEach((job: JobDataType) => {
        if (!yearMap[job.work_year]) {
          yearMap[job.work_year] = { totalJobs: 0, totalSalary: 0 };
        }
        yearMap[job.work_year].totalJobs += 1;
        yearMap[job.work_year].totalSalary += job.salary_in_usd;
      });
      console.log(yearMap);

      const aggregatedArray: AggregatedData[] = Object.entries(yearMap).map(
        ([year, { totalJobs, totalSalary }]) => ({
          year: parseInt(year, 10),
          totalJobs,
          averageSalary: totalSalary / totalJobs,
        })
      );

      setAggregatedData(aggregatedArray);
    };

    aggregateDataHandler();
  }, []);

  const handleSort = (column: keyof AggregatedData) => {
    const direction =
      sortColumn === column && sortDirection === "asc" ? "desc" : "asc";
    setSortColumn(column);
    setSortDirection(direction);
  };

  const sortedData = [...aggregatedData].sort((a, b) => {
    if (a[sortColumn] < b[sortColumn]) return sortDirection === "asc" ? -1 : 1;
    if (a[sortColumn] > b[sortColumn]) return sortDirection === "asc" ? 1 : -1;
    return 0;
  });

  const getSortIcon = (column: keyof AggregatedData) => {
    if (sortColumn === column) {
      return sortDirection === "asc" ? "▲" : "▼";
    }
    return "▲▼";
  };

  const handleRowClick = (year: number) => {
    setSelectedYear(year);
    setShowTable((prev) => !prev);
    const titlesMap: { [key: string]: number } = {};

    data.forEach((job: JobDataType) => {
      if (job.work_year === year) {
        if (!titlesMap[job.job_title]) {
          titlesMap[job.job_title] = 0;
        }
        titlesMap[job.job_title] += 1;
      }
    });

    const titlesArray: JobTitleData[] = Object.entries(titlesMap).map(
      ([job_title, count]) => ({
        job_title,
        count,
      })
    );

    setJobTitles(titlesArray);
  };

  return (
    <>
      <table>
        <thead>
          <tr>
            <th onClick={() => handleSort("year")}>
              Year {getSortIcon("year")}
            </th>
            <th onClick={() => handleSort("totalJobs")}>
              Number of Total Jobs {getSortIcon("totalJobs")}
            </th>
            <th onClick={() => handleSort("averageSalary")}>
              Average Salary in USD {getSortIcon("averageSalary")}
            </th>
          </tr>
        </thead>
        <tbody>
          {sortedData.map((row) => (
            <tr key={row.year} onClick={() => handleRowClick(row.year)}>
              <td>{row.year}</td>
              <td>{row.totalJobs}</td>
              <td>{row.averageSalary.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {showTable ? (
        <div>
          <h2>Job Titles for {selectedYear}</h2>
          <table>
            <thead>
              <tr>
                <th>Job Title</th>
                <th>Total Jobs</th>
              </tr>
            </thead>
            <tbody>
              {jobTitles.map((title) => (
                <tr key={title.job_title}>
                  <td>{title.job_title}</td>
                  <td>{title.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : null}
     
    </>
  );
};

export default Table;
