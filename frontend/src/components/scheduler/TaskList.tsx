import {useEffect, useState} from "react";
import { Task, ApiService } from "../../api";
import * as React from 'react';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';



const columns = [
  { id: 'task_date', label: 'Date', minWidth: 100 },
  { id: 'technology', label: 'Technology', minWidth: 100 },
  {
    id: 'airline',
    label: 'Airline',
    minWidth: 170,
    align: 'right',
    format: (value: { toLocaleString: (arg0: string) => any; }) => value.toLocaleString('en-US'),
  },
  {
    id: 'aircraft_type',
    label: 'Aircraft type',
    minWidth: 170,
    align: 'right',
    format: (value: { toLocaleString: (arg0: string) => any; }) => value.toLocaleString('en-US'),
  },
  {
    id: 'registration',
    label: 'Registration',
    minWidth: 170,
    align: 'right',

  },
  {
    id: 'sched_time',
    label: 'Schedule time',
    minWidth: 170,
    align: 'right',
  },

];

function TaskItem(props: Task) {
   
    const [open, setOpen] = React.useState(false);
     return <div>
      
      
      <Paper sx={{ width: '100%', mb: 2 }}>
            <TableRow hover>
              
              <TableCell>
                <IconButton
                  aria-label="expand row"
                  size="small"
                  onClick={() => setOpen(!open)}
                >
                  {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                </IconButton>
              </TableCell>
              <TableCell component="th" scope="row">
                {props.task_date}
              </TableCell>
              <TableCell>{props.technology}</TableCell>
              <TableCell>{props.airline}</TableCell>
              <TableCell>{props.aircraft_type}</TableCell>
              <TableCell>{props.registration}</TableCell>
              <TableCell>{props.sched_time}</TableCell>
              <TableCell>{props.status}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                <Collapse in={open} timeout="auto" unmountOnExit>
                  <Box sx={{ margin: 1 }}>
                    <Typography variant="h6" gutterBottom component="div">
                      Detail
                    </Typography>
                    <Table size="small" aria-label="purchases">
                      <TableHead>
                        <TableRow>
                          <TableCell>set by:</TableCell>
                          <TableCell>route</TableCell>
                          <TableCell>payload</TableCell>
                          <TableCell>description</TableCell>
                          <TableCell>is Return?</TableCell>
                          <TableCell>record create</TableCell>
                          <TableCell>record update</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        
                          <TableRow
                            >
                            <TableCell>{props.user}</TableCell>
                            <TableCell>{props.route}</TableCell>
                            <TableCell>{props.payload}</TableCell>
                            <TableCell>{props.description}</TableCell>
                            <TableCell>{props.is_return}</TableCell>
                            <TableCell>{props.create_at}</TableCell>
                            <TableCell>{props.update_at}</TableCell>
                            
                          </TableRow>
                        
                      </TableBody>
                    </Table>
                  </Box>
                </Collapse>
              </TableCell>
            </TableRow>
 . . . </Paper>
          
         
         
     
      
    
    </div>;
}

export default function TaskList() {
    const [tasks, setTasks] = useState<Task[] | undefined>();
    const loadTasks = async () => {
        setTasks(await ApiService.apiAirlinesList());
    }
    useEffect(() => {
        loadTasks();
    }, []);
    return (
        <div>
            <h1>Flights:</h1>
            {/* <TableContainer component={Paper}>
                <Table aria-label="collapsible table">
                    <TableHead>
                      <TableRow>
                        {columns.map((column) => (
                          <TableCell
                            key={column.id}
                            style={{ minWidth: column.minWidth }}
                          >
                            {column.label}
                          </TableCell>
                        ))}
                      </TableRow>
                    </TableHead>
                    <TableBody>
                
                    </TableBody>
                </Table>
            </TableContainer> */}
            {tasks && tasks.map(
                task => {
                    return <TaskItem {...task}/>;
                })}
        </div>
    );
}