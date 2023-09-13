/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_auth_get_token } from '../models/Body_auth_get_token';
import type { RegisterPost } from '../models/RegisterPost';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AuthService {

    /**
     * Get Token
     * @param formData 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static authGetToken(
formData: Body_auth_get_token,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/auth/token',
            formData: formData,
            mediaType: 'application/x-www-form-urlencoded',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Register
     * @param requestBody 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static authRegister(
requestBody: RegisterPost,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/auth/register',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Refresh Access Token
     * @param refreshToken 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static authRefreshAccessToken(
refreshToken: string,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/auth/refresh',
            query: {
                'refresh_token': refreshToken,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
