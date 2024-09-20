import { useMemo, useState } from "react";
import {
  STLInputObjectValues,
  useSTLInputContext,
} from "../../context/STLInputs";
import styled from "styled-components";
import { isEqual } from "lodash";
import { NumberInput } from "./NumberInput";
import { MAX_BED_SIZE } from "../../constants";
import { ArrowCircleRight, DownloadSimple } from "@phosphor-icons/react";
import { SwitchInput } from "./SwitchInput";

const StyledSTLInputs = styled.div`
  position: relative;
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
  align-content: start;
  padding: 24px 12px;
`;

const InputCategory = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
`;

const GENERATE_BUTTON_SIZE = 36;
const GenerateButton = styled.button`
  position: absolute;
  display: grid;
  place-items: center;
  top: 36px;
  right: -60px;
  z-index: +1;
  border: 0;
  outline: none;
  padding: 0;
  margin: 0;
  width: ${GENERATE_BUTTON_SIZE}px;
  height: ${GENERATE_BUTTON_SIZE}px;
  background-color: #eee;
  border-radius: ${GENERATE_BUTTON_SIZE}px;
  border: 1px solid blue;

  &:disabled {
    opacity: 0.25;
    cursor: not-allowed;
  }
`;

const DownloadLink = styled.a`
  display: grid;
  place-items: center;
  width: ${GENERATE_BUTTON_SIZE - 2}px;
  height: ${GENERATE_BUTTON_SIZE - 2}px;
  background-color: #eee;
  position: fixed;
  top: calc(36px + 36px);
  right: 24px;
  z-index: +1;
  border-radius: ${GENERATE_BUTTON_SIZE}px;
  border: 1px solid blue;

  &.disabled {
    opacity: 0.25;
    pointer-events: none;
  }
`;

export default function STLInputs() {
  const { setValues, url, ...defaultValues } = useSTLInputContext();

  const [slotSizeX, setSlotSizeX] = useState<number>(defaultValues.slotSizeX);
  const [slotSizeY, setSlotSizeY] = useState<number>(defaultValues.slotSizeY);
  const [slotSizeZ, setSlotSizeZ] = useState<number>(defaultValues.slotSizeZ);
  const [numberOfSlotsX, setNumberOfSlotsX] = useState<number>(
    defaultValues.numberOfSlotsX
  );
  const [numberOfSlotsY, setNumberOfSlotsY] = useState<number>(
    defaultValues.numberOfSlotsY
  );
  const [wallThickness, setWallThickness] = useState<number>(
    defaultValues.wallThickness
  );
  const [wallInset, setWallInset] = useState<number>(defaultValues.wallInset);
  const [withLidInset, setWithLidInset] = useState<boolean>(
    defaultValues.withLidInset
  );
  const [withPullTab, setWithPullTab] = useState<boolean>(
    defaultValues.withPullTab
  );

  const handleGenerate = () => {
    setValues({
      slotSizeX,
      slotSizeY,
      slotSizeZ,
      numberOfSlotsX,
      numberOfSlotsY,
      wallThickness,
      wallInset,
      withLidInset,
      withPullTab,
    });
  };

  const downloadUrl = useMemo(() => {
    const serverUrl = process.env.REACT_APP_SERVER_URL;
    return `${serverUrl}${url}`;
  }, [url]);

  const inputsValues: STLInputObjectValues = useMemo(() => {
    return {
      slotSizeX,
      slotSizeY,
      slotSizeZ,
      numberOfSlotsX,
      numberOfSlotsY,
      wallThickness,
      wallInset,
      withLidInset,
      withPullTab,
    };
  }, [
    slotSizeX,
    slotSizeY,
    slotSizeZ,
    numberOfSlotsX,
    numberOfSlotsY,
    wallThickness,
    wallInset,
    withLidInset,
    withPullTab,
  ]);

  const generateButtonIsActive = useMemo(() => {
    const currentContextValues: STLInputObjectValues = {
      slotSizeX: defaultValues.slotSizeX,
      slotSizeY: defaultValues.slotSizeY,
      slotSizeZ: defaultValues.slotSizeZ,
      numberOfSlotsX: defaultValues.numberOfSlotsX,
      numberOfSlotsY: defaultValues.numberOfSlotsY,
      wallThickness: defaultValues.wallThickness,
      wallInset: defaultValues.wallInset,
      withLidInset: defaultValues.withLidInset,
      withPullTab: defaultValues.withPullTab,
    };

    return !isEqual(inputsValues, currentContextValues);
  }, [defaultValues, inputsValues]);

  return (
    <StyledSTLInputs>
      <InputCategory>
        <h2>Slot Size:</h2>
        <NumberInput
          label="Slot Size X"
          onChange={setSlotSizeX}
          defaultValue={slotSizeX}
        />
        <NumberInput
          label="Slot Size Y"
          onChange={setSlotSizeY}
          defaultValue={slotSizeY}
        />
        <NumberInput
          label="Slot Size Z"
          onChange={setSlotSizeZ}
          defaultValue={slotSizeZ}
        />
      </InputCategory>

      <InputCategory>
        <h2>Number of Slots:</h2>
        <NumberInput
          label="Number of Slots X"
          onChange={setNumberOfSlotsX}
          defaultValue={numberOfSlotsX}
          max={Math.round(MAX_BED_SIZE / slotSizeX)}
        />
        <NumberInput
          label="Number of Slots Y"
          onChange={setNumberOfSlotsY}
          defaultValue={numberOfSlotsY}
          max={Math.round(MAX_BED_SIZE / slotSizeY)}
        />
      </InputCategory>

      <InputCategory>
        <h2>Walls:</h2>

        <NumberInput
          label="Wall Thickness"
          onChange={setWallThickness}
          defaultValue={wallThickness}
          max={Math.min(slotSizeX, slotSizeY)}
        />

        <NumberInput
          label="Wall Inset"
          onChange={setWallInset}
          defaultValue={wallInset}
          max={slotSizeZ - 1}
        />
      </InputCategory>

      <InputCategory>
        <h2>Lid Options:</h2>

        <SwitchInput
          label="With lid inset"
          defaultValue={withLidInset}
          onChange={setWithLidInset}
        />

        <SwitchInput
          label="With pull tab"
          defaultValue={withPullTab}
          onChange={setWithPullTab}
        />
      </InputCategory>

      <div>
        <GenerateButton
          onClick={handleGenerate}
          disabled={!generateButtonIsActive}
        >
          <ArrowCircleRight
            size={GENERATE_BUTTON_SIZE - 10}
            weight="duotone"
            color="#0000ff"
          />
        </GenerateButton>
        <DownloadLink
          href={downloadUrl}
          download="vssl-output.stl"
          className={generateButtonIsActive ? "disabled" : ""}
        >
          <DownloadSimple
            size={GENERATE_BUTTON_SIZE - 10}
            weight="duotone"
            color="#0000ff"
          />
        </DownloadLink>
      </div>
    </StyledSTLInputs>
  );
}
