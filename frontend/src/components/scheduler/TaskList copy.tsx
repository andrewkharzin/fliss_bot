import {useEffect, useState} from "react";
import { Task, ApiService } from "../../api";
import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import ImageIcon from '@mui/icons-material/Image';
import WorkIcon from '@mui/icons-material/Work';
import BeachAccessIcon from '@mui/icons-material/BeachAccess';

function TaskItem(props: Task) {
    return <div>
        <p>{props.task_date}</p>
        <b>{props.technology}</b>
        <b>{props.airline}</b>
        <b>{props.aircraft_type}</b>
        <b>{props.registration}</b>
        <b>{props.sched_time}</b>
        <b>{props.route}</b>
        <b>{props.payload}</b>
        <b>{props.description}</b>
        <b>{props.status}</b>
        <b>{props.is_return}</b>
    </div>;
}

export default function TaskList() {
    const [tasks, setTasks] = useState<Task[] | undefined>();
    const loadTasks = async () => {
        setTasks(await ApiService.apiSchedulerList());
    }
    useEffect(() => {
        loadTasks();
    }, []);
    return (
        <div>
            <h1>Flights:</h1>
            {tasks && tasks.map(
                task => {
                    return <TaskItem {...task}/>;
                })}
        </div>
    );
}