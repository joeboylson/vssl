import { FallbackProps } from "react-error-boundary";
import styled from "styled-components";

const StyledFallbackRender = styled.div`
  display: grid;
  place-items: center;
  max-width: 400px;
`;

export default function FallbackRender({ error }: FallbackProps) {
  const errorMessageString: string = error.message.toString();

  if (errorMessageString.includes("TOO MANY REQUESTS"))
    return (
      <StyledFallbackRender>
        <div>
          <b>Hey there! Joe here. Looks like you're really enjoying VSSL!</b>
          <br /> <br />
          <p>
            Unfortunately, you've reached your request limit for now. Since the
            app is currently in its alpha version, I've set limits on how many
            requests can be made in a short period top keep costs low (50/hour).
            Please try again in a bit once the system resets.
          </p>
          <br />
          <p>
            If you have any issues, feature suggestions, or just want to share
            your thoughts, feel free to reach out to me at
            [joeboylson@gmail.com]. I appreciate your understanding and feedback
            as I continue to work on this app.
          </p>
          <br />
          <p>Thanks again!</p>
        </div>
      </StyledFallbackRender>
    );

  return (
    <StyledFallbackRender>
      <div>
        <strong>Oops! Looks like something went wrong:</strong>
        <p>{error.message}</p>
      </div>
    </StyledFallbackRender>
  );
}
