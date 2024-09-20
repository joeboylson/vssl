import { useEffect, useState } from "react";
import { useAuthenticatedUser } from "../../hooks/useAuthenticatedUser";
import styled from "styled-components";

const StyledLogin = styled.div`
  width: 100vw;
  height: 100vh;
  display: grid;
  place-items: center;
`;

const LoginLink = styled.button`
  display: block;
  text-align: center;
  text-decoration: none;
  border: 1px solid black;
  color: black;
  padding: 12px 32px;
  border-radius: 50px;
  font-size: 16px;
`;

export default function Login() {
  const { sendOTPToken, verifyOTPToken, otpTokenIsSent, loading } =
    useAuthenticatedUser({
      skipAuthenticatedUserQuery: true,
    });

  const [email, setEmail] = useState<string>();
  const [token, setToken] = useState<string>();

  if (loading) return <p>loading...</p>;

  return (
    <StyledLogin>
      {otpTokenIsSent ? (
        <div>
          <input
            type="text"
            placeholder="OTP"
            onChange={(e) => setToken(e.target.value)}
          />
          <button onClick={() => verifyOTPToken(email, token)}>Submit</button>
        </div>
      ) : (
        <div>
          <input
            type="text"
            name="email"
            placeholder="Email"
            onChange={(e) => setEmail(e.target.value)}
          />
          <button onClick={() => sendOTPToken(email)}>Submit</button>
        </div>
      )}
    </StyledLogin>
  );
}
