import styled from "styled-components";
import { HEADER_HEIGHT } from "../../constants";
import { useAuthenticatedUser } from "../../hooks/useAuthenticatedUser";

const StyledHeader = styled.div`
  height: ${HEADER_HEIGHT}px;
  background-color: black;
  color: white;
`;

export default function Header() {
  const { authenticatedUser } = useAuthenticatedUser();

  if (!authenticatedUser) return <StyledHeader />;

  return (
    <StyledHeader>
      <p>{authenticatedUser.user?.email}</p>
    </StyledHeader>
  );
}
