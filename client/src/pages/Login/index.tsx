import { useCallback, useState } from "react";
import { useAuthenticatedUser } from "../../hooks/useAuthenticatedUser";
import styled from "styled-components";
import Loading from "../../components/Loading";
import { Button, TextField } from "@mui/material";

const StyledLogin = styled.div`
  width: 100vw;
  height: 100vh;
  display: grid;
  place-items: center;
`;

const StyledLoginInner = styled.div`
  width: 100%;
  max-width: 400px;
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
`;

export default function Login() {
  const { sendOTPToken, verifyOTPToken, otpTokenIsSent, loading } =
    useAuthenticatedUser({
      skipAuthenticatedUserQuery: true,
    });

  const [email, setEmail] = useState<string>();
  const [token, setToken] = useState<string>();

  const handleClick = useCallback(() => {
    if (otpTokenIsSent) return verifyOTPToken(email, token);
    return sendOTPToken(email);
  }, [email, otpTokenIsSent, sendOTPToken, token, verifyOTPToken]);

  return (
    <StyledLogin>
      <StyledLoginInner>
        <TextField
          size="small"
          type="text"
          name="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
          disabled={loading || otpTokenIsSent}
          defaultValue={email}
        />

        {otpTokenIsSent && (
          <TextField
            size="small"
            type="text"
            placeholder="OTP"
            onChange={(e) => setToken(e.target.value)}
          />
        )}

        <Button onClick={handleClick} variant="contained" disabled={loading}>
          {loading ? "Loading..." : "Submit"}
        </Button>
      </StyledLoginInner>
    </StyledLogin>
  );
}
