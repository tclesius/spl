/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { InvitePost } from '../models/InvitePost';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class InviteService {

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
