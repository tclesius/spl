/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreateRelease } from '../models/CreateRelease';
import type { InvitePost } from '../models/InvitePost';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AdminService {

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

    /**
     * Revoke an invite
     * @param inviteId 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static inviteRevoke(
inviteId: number,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/invite/revoke',
            query: {
                'invite_id': inviteId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Invite a user
     * @param requestBody 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static inviteSend(
requestBody: InvitePost,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/invite/send',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Resend an invite
     * @param inviteId 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static inviteResend(
inviteId: number,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/invite/resend',
            query: {
                'invite_id': inviteId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
