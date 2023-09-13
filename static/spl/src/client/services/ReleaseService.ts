/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreateRelease } from '../models/CreateRelease';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class ReleaseService {

    /**
     * Get Latest Release
     * @returns any Successful Response
     * @throws ApiError
     */
    public static releaseGetLatestRelease(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/release/latest',
        });
    }

    /**
     * Create Release
     * @param requestBody 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static releaseCreateRelease(
requestBody: CreateRelease,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/release/create',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Remove Release
     * @param releaseId 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static releaseRemoveRelease(
releaseId: number,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/release/remove',
            query: {
                'release_id': releaseId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
