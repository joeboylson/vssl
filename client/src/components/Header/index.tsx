import styled from "styled-components";
import { HEADER_HEIGHT } from "../../constants";
import { useAuthenticatedUser } from "../../hooks/useAuthenticatedUser";
import { Info } from "@phosphor-icons/react";
import { useToggle } from "../../hooks/useToggle";
import AppInformationModal from "../AppInformationModal";

const StyledHeader = styled.div`
  height: ${HEADER_HEIGHT}px;
  background-color: black;
  color: white;
  display: flex;
  align-items: center;
`;

const LogoWrapper = styled.div`
  width: calc(${HEADER_HEIGHT}px - 16px - 16px);
  height: calc(${HEADER_HEIGHT}px - 16px - 16px);
  margin: 8px 16px 8px 8px;
  padding: 4px;
  background-color: #0000ff;
  border-radius: ${HEADER_HEIGHT}px;
  overflow: hidden;
`;

const Logo = styled.img`
  width: 100%;
`;

const ProfileName = styled.p`
  font-family: Elios;
  font-size: 12px;
`;

const InfoButton = styled.button`
  width: 24px;
  height: 24px;
  margin: 12px;
  padding: 0;
  display: grid;
  place-items: center;
  justify-self: end;
  margin-left: auto;
  background-color: transparent;
  outline: none;
  border: 0;
`;

export default function Header() {
  const {
    value: modalIsOpen,
    enable: openModal,
    disable: closeModal,
  } = useToggle();

  const { authenticatedUser } = useAuthenticatedUser();
  if (!authenticatedUser) return <StyledHeader />;

  return (
    <StyledHeader>
      <LogoWrapper>
        <Logo src={"logo.png"} />
      </LogoWrapper>
      <ProfileName>Hey there, {authenticatedUser.user?.email}</ProfileName>

      <InfoButton onClick={openModal}>
        <Info size={20} color="#FFFFFF" weight="duotone" />
      </InfoButton>

      <AppInformationModal open={modalIsOpen} onClose={closeModal} />
    </StyledHeader>
  );
}
