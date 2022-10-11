/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type Task = {
    readonly id?: string;
    readonly user?: string;
    task_date: string;
    technology?: Task.technology;
    readonly airline?: string;
    aircraft_type?: string;
    readonly registration?: string;
    flight?: string;
    sched_time?: string | null;
    route?: string;
    payload?: string;
    description?: string;
    status?: Task.status;
    readonly slug?: string;
    is_return?: boolean;
    readonly create_at?: string;
    readonly update_at?: string;
};

export namespace Task {

    export enum technology {
        ARRIVAL = 'arrival',
        DEPARTURE = 'departure',
    }

    export enum status {
        DRAFT = 'draft',
        COMPLETED = 'completed',
        INPROGRESS = 'inprogress',
        CANCELED = 'canceled',
        STAND_BY = 'standBy',
    }


}

