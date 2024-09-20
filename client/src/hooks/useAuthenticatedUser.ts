import axios from "axios";
import { isEmpty } from "lodash";
import { useCallback, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { User } from "@supabase/supabase-js";

interface _options {
  skipAuthenticatedUserQuery: boolean;
}

// TODO
export type IsAuthenticated = {
  user?: User;
};

export function useAuthenticatedUser(options?: _options) {
  const navigate = useNavigate();

  const [loading, setLoading] = useState<boolean>(false);
  const [authenticationUrl, setAuthenticationUrl] = useState<string>();
  const [authenticatedUser, setAuthenticatedUser] = useState<IsAuthenticated>();

  const [otpTokenIsSent, setOTPTokenIsSent] = useState<boolean>(false);

  const getIsAuthenticated = useCallback(async () => {
    if (authenticatedUser) return;
    setLoading(true);

    try {
      const response = await axios.get(`/is-authenticated`);
      const _authenticatedUser = response.data as unknown as IsAuthenticated;

      if (isEmpty(_authenticatedUser?.user)) {
        throw new Error("Invalid user");
      }

      setAuthenticatedUser(_authenticatedUser);
    } catch (error) {
      console.error(error);
      navigate("/login");
    } finally {
      setLoading(false);
    }
  }, [navigate, authenticatedUser]);

  const sendOTPToken = useCallback(
    async (email?: string) => {
      setLoading(true);
      if (!email) return;

      try {
        const response = await axios.get(`/send-otp-token?email=${email}`);
        setOTPTokenIsSent(response.data.success ?? false);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    },
    [authenticationUrl]
  );

  const verifyOTPToken = useCallback(
    async (email?: string, token?: string) => {
      setLoading(true);
      if (!token || !email) return;

      try {
        await axios.get(`/verify-otp-token?email=${email}&token=${token}`);
        navigate("/");
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    },
    [authenticationUrl]
  );

  const logout = useCallback(async () => {
    try {
      setLoading(true);
      // TODO
      await axios.get(`/api/auth/logout`);
      navigate("/login");
    } finally {
      setLoading(false);
    }
  }, [navigate]);

  useEffect(() => {
    if (!options?.skipAuthenticatedUserQuery) getIsAuthenticated();
  }, [getIsAuthenticated, options]);

  const exportFunctions = {
    sendOTPToken,
    verifyOTPToken,
    logout,
  };

  const exportValues = {
    otpTokenIsSent,
    loading,
    authenticatedUser,
    authenticationUrl,
  };

  return { ...exportFunctions, ...exportValues };
}
