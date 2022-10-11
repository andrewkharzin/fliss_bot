/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Airline } from '../models/Airline';
import type { Register } from '../models/Register';
import type { Task } from '../models/Task';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class ApiService {

    /**
     * @param page A page number within the paginated result set.
     * @returns any
     * @throws ApiError
     */
    public static apiAirlinesList(
        page?: number,
    ): CancelablePromise<{
        count: number;
        next?: string | null;
        previous?: string | null;
        results: Array<Airline>;
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/airlines/',
            query: {
                'page': page,
            },
        });
    }

    /**
     * @param data
     * @returns Airline
     * @throws ApiError
     */
    public static apiAirlinesCreate(
        data: Airline,
    ): CancelablePromise<Airline> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/airlines/',
            body: data,
        });
    }

    /**
     * @param page A page number within the paginated result set.
     * @returns any
     * @throws ApiError
     */
    public static apiRegistersList(
        page?: number,
    ): CancelablePromise<{
        count: number;
        next?: string | null;
        previous?: string | null;
        results: Array<Register>;
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/registers/',
            query: {
                'page': page,
            },
        });
    }

    /**
     * @param data
     * @returns Register
     * @throws ApiError
     */
    public static apiRegistersCreate(
        data: Register,
    ): CancelablePromise<Register> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/registers/',
            body: data,
        });
    }

    /**
     * @param page A page number within the paginated result set.
     * @returns any
     * @throws ApiError
     */
    public static apiSchedulerList(
        page?: number,
    ): CancelablePromise<{
        count: number;
        next?: string | null;
        previous?: string | null;
        results: Array<Task>;
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/scheduler/',
            query: {
                'page': page,
            },
        });
    }

    /**
     * @param data
     * @returns Task
     * @throws ApiError
     */
    public static apiSchedulerCreate(
        data: Task,
    ): CancelablePromise<Task> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/scheduler/',
            body: data,
        });
    }

    /**
     * @param pkid A unique integer value identifying this FlightTask.
     * @returns Task
     * @throws ApiError
     */
    public static apiRead(
        pkid: number,
    ): CancelablePromise<Task> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/{pkid}',
            path: {
                'pkid': pkid,
            },
        });
    }

    /**
     * @param pkid A unique integer value identifying this FlightTask.
     * @returns void
     * @throws ApiError
     */
    public static apiDelete(
        pkid: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/{pkid}',
            path: {
                'pkid': pkid,
            },
        });
    }

}
