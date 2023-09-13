/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UserService {

    /**
     * Change password
     * @param newPassword 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static userChangeMyPassword(
newPassword: string,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/user/change-password',
            query: {
                'new_password': newPassword,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Remove a user
     * @param userId 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static userRemoveUser(
userId: number,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/user/remove',
            query: {
                'user_id': userId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Search for a user
     * @param username 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static userSearchUser(
username: string,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/search',
            query: {
                'username': username,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get all users
     * @returns any Successful Response
     * @throws ApiError
     */
    public static userGetAllUser(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/all',
        });
    }

    /**
     * Get your own user data
     * @returns any Successful Response
     * @throws ApiError
     */
    public static userGetMe(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/me',
        });
    }

    /**
     * Check if username is available
     * @param inviteToken 
     * @param username 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static userCheckUsername(
inviteToken: string,
username: string,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/usercheck-username',
            query: {
                'invite_token': inviteToken,
                'username': username,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
